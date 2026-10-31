import streamlit as st, py3Dmol
import streamlit.components.v1 as components
from utils.ui import setup, hero, footer
from utils import chem

setup("Molecule Viewer", "🔬")
hero("Molecule Viewer", "Visualise a structure in 2D and 3D.")

sample = st.selectbox("Start from an example", ["Custom"] + list(chem.SAMPLES))
smiles = st.text_input("SMILES", value=chem.SAMPLES.get(sample, ""), placeholder="e.g. CC(=O)OC1=CC=CC=C1C(=O)O")

if smiles:
    mol = chem.parse(smiles)
    if mol is None:
        st.error("That doesn't look like a valid SMILES string. Check brackets, ring numbers and atom symbols.")
    else:
        t2d, t3d = st.tabs(["2D", "3D"])
        with t2d:
            svg = chem.mol_svg(mol)
            st.markdown(f'<div class="mol-box">{svg}</div>', unsafe_allow_html=True)
            st.download_button("Download SVG", svg, "molecule.svg", "image/svg+xml")
        with t3d:
            style = st.radio("Style", ["stick", "sphere", "line"], horizontal=True)
            with st.spinner("Generating 3D conformer…"):
                block = chem.mol_block_3d(smiles)
            if block is None:
                st.warning("Could not generate a 3D conformer for this molecule.")
            else:
                v = py3Dmol.view(width=700, height=450)
                v.addModel(block, "mol")
                v.setStyle({style: {}})
                v.setBackgroundColor("white")
                v.zoomTo()
                components.html(v._make_html(), height=460)
                st.download_button("Download MOL file", block, "molecule.mol")
else:
    st.info("Enter a SMILES string or pick an example to begin.")
footer()
