import io, streamlit as st, pandas as pd, plotly.express as px
from rdkit import Chem
from utils.ui import setup, hero, footer
from utils import chem

setup("Dataset Explorer", "📊")
hero("Dataset Explorer", "Upload, filter and visualise molecular datasets.")

@st.cache_data(show_spinner=False)
def enrich(smiles_list):
    return pd.DataFrame([p for p in (chem.properties(s) for s in smiles_list) if p])

f = st.file_uploader("Upload CSV or SDF", type=["csv", "sdf"])
use_sample = st.checkbox("Use built-in sample set", value=f is None)

smiles = None
if f is not None:
    if f.name.lower().endswith(".csv"):
        raw = pd.read_csv(f)
        idx = next((i for i, c in enumerate(raw.columns) if "smiles" in c.lower()), 0)
        col = st.selectbox("SMILES column", raw.columns, index=idx)
        smiles = tuple(raw[col].dropna().astype(str))
    else:
        sup = Chem.ForwardSDMolSupplier(io.BytesIO(f.read()))
        smiles = tuple(Chem.MolToSmiles(m) for m in sup if m is not None)
elif use_sample:
    smiles = tuple(chem.SAMPLES.values())

if not smiles:
    st.info("Upload a file or tick the sample set.")
else:
    with st.spinner("Computing properties…"):
        df = enrich(smiles)
    if df.empty:
        st.error("No valid molecules found. Check the SMILES column.")
    else:
        st.caption(f"{len(df)} valid of {len(smiles)} molecules")
        lo, hi = float(df.MW.min()), float(df.MW.max()) + 0.01
        c1, c2 = st.columns(2)
        mw = c1.slider("Molecular weight", lo, hi, (lo, hi))
        only = c2.toggle("Lipinski-compliant only")
        d = df[df.MW.between(*mw)]
        if only:
            d = d[d["Passes Ro5"]]
        t1, t2, t3 = st.tabs(["Table", "Scatter", "Histogram"])
        t1.dataframe(d, use_container_width=True, hide_index=True)
        with t2:
            x = st.selectbox("X", ["MW", "LogP", "TPSA", "HBD", "HBA"], 0)
            y = st.selectbox("Y", ["MW", "LogP", "TPSA", "HBD", "HBA"], 1)
            st.plotly_chart(px.scatter(d, x=x, y=y, color="Passes Ro5", hover_data=["SMILES"]), use_container_width=True)
        with t3:
            h = st.selectbox("Property", ["MW", "LogP", "TPSA", "RotBonds"])
            st.plotly_chart(px.histogram(d, x=h, color_discrete_sequence=["#0071E3"]), use_container_width=True)
        st.download_button("Download filtered CSV", d.to_csv(index=False), "filtered.csv", "text/csv")
footer()
