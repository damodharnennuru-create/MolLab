import streamlit as st
from utils.ui import setup, hero, footer

setup("Home", "🧪")
hero("Cheminformatics Virtual Lab", "Explore molecules, predict drug-likeness and search chemical space — all in your browser.")

cards = [
    ("🔬", "Molecule Viewer", "Draw any SMILES in 2D and rotate it in interactive 3D."),
    ("⚗️", "Property Calculator", "MW, LogP, TPSA, HBD/HBA and a Lipinski rule-of-five check."),
    ("🧬", "Similarity Search", "Rank a library by Tanimoto similarity using Morgan fingerprints."),
    ("📊", "Dataset Explorer", "Upload CSV or SDF files, filter by property and plot with Plotly."),
]
html = '<div class="card-grid">' + "".join(
    f'<div class="card"><div class="icon">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in cards) + "</div>"
st.markdown(html, unsafe_allow_html=True)
st.caption("Use the sidebar to open a tool.")
footer()
