import streamlit as st, pandas as pd, plotly.express as px
from rdkit import DataStructs
from utils.ui import setup, hero, footer
from utils import chem

setup("Similarity Search", "🧬")
hero("Similarity Search", "Find the closest molecules by Tanimoto similarity.")

q = st.text_input("Query SMILES", chem.SAMPLES["Aspirin"])
lib = st.text_area("Library (one per line: 'name,SMILES' or just SMILES)",
                   "\n".join(f"{n},{s}" for n, s in chem.SAMPLES.items()), height=150)
c1, c2 = st.columns(2)
radius = c1.slider("Morgan radius", 1, 4, 2)
nbits = c2.select_slider("Bits", [512, 1024, 2048, 4096], 2048)

if st.button("Search"):
    qm = chem.parse(q)
    if qm is None:
        st.error("Invalid query SMILES.")
    else:
        qfp = chem.fingerprint(qm, radius, nbits)
        rows = []
        with st.spinner("Comparing fingerprints…"):
            for i, line in enumerate(l for l in lib.splitlines() if l.strip()):
                name, smi = line.split(",", 1) if "," in line else (f"mol_{i+1}", line)
                m = chem.parse(smi)
                if m is not None:
                    sim = DataStructs.TanimotoSimilarity(qfp, chem.fingerprint(m, radius, nbits))
                    rows.append({"Name": name.strip(), "SMILES": smi.strip(), "Tanimoto": round(sim, 3)})
        if not rows:
            st.warning("No valid molecules in the library.")
        else:
            df = pd.DataFrame(rows).sort_values("Tanimoto", ascending=False)
            fig = px.bar(df, x="Name", y="Tanimoto", color="Tanimoto", color_continuous_scale=["#D2D2D7", "#0071E3"])
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.download_button("Download CSV", df.to_csv(index=False), "similarity.csv", "text/csv")
footer()
