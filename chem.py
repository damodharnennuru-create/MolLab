import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors, AllChem
from rdkit.Chem.Draw import rdMolDraw2D

SAMPLES = {
    "Aspirin": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "Caffeine": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
    "Ibuprofen": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
    "Paracetamol": "CC(=O)NC1=CC=C(O)C=C1",
    "Naproxen": "COC1=CC2=CC=C(C=C2C=C1)C(C)C(=O)O",
    "Metformin": "CN(C)C(=N)N=C(N)N",
}

def parse(smiles):
    smiles = (smiles or "").strip()
    return Chem.MolFromSmiles(smiles) if smiles else None

def mol_svg(mol, size=(420, 320)):
    d = rdMolDraw2D.MolDraw2DSVG(*size)
    d.drawOptions().clearBackground = False
    d.DrawMolecule(mol)
    d.FinishDrawing()
    return d.GetDrawingText()

@st.cache_data(show_spinner=False)
def properties(smiles):
    m = Chem.MolFromSmiles(smiles)
    if m is None:
        return None
    mw, logp = Descriptors.MolWt(m), Crippen.MolLogP(m)
    hbd, hba = rdMolDescriptors.CalcNumHBD(m), rdMolDescriptors.CalcNumHBA(m)
    viol = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
    return {
        "SMILES": smiles, "MW": round(mw, 2), "LogP": round(logp, 2),
        "TPSA": round(rdMolDescriptors.CalcTPSA(m), 2), "HBD": hbd, "HBA": hba,
        "RotBonds": rdMolDescriptors.CalcNumRotatableBonds(m),
        "Rings": rdMolDescriptors.CalcNumRings(m),
        "Lipinski violations": viol, "Passes Ro5": viol <= 1,
    }

def fingerprint(mol, radius=2, nbits=2048):
    return AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nbits)

@st.cache_data(show_spinner=False)
def mol_block_3d(smiles):
    m = Chem.AddHs(Chem.MolFromSmiles(smiles))
    if AllChem.EmbedMolecule(m, randomSeed=42) != 0:
        return None
    try:
        AllChem.MMFFOptimizeMolecule(m)
    except Exception:
        pass
    return Chem.MolToMolBlock(m)
