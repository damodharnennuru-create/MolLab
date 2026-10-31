import streamlit as st
from utils.ui import setup, hero, footer

setup("About", "ℹ️")
hero("About", "An independent, educational cheminformatics toolkit.")
st.markdown("""
Built with **Streamlit**, **RDKit**, **Plotly**, **py3Dmol**, **pandas** and **NumPy**.

- Molecule Viewer: 2D (RDKit SVG) and 3D (ETKDG + MMFF)
- Property Calculator: Crippen LogP, TPSA, Lipinski rule of five
- Similarity Search: Morgan fingerprints and Tanimoto
- Dataset Explorer: CSV/SDF upload, filtering, Plotly charts

Lipinski's rule of five is a heuristic, not a guarantee of drug-likeness.
""")
footer()
