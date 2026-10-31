import streamlit as st, pandas as pd
from utils.ui import setup, hero, footer
from utils import chem

setup("Property Calculator", "⚗️")
hero("Property Calculator", "Drug-likeness at a glance.")

txt = st.text_area("SMILES (one per line)", value=chem.SAMPLES["Aspirin"], height=140)
lines = [s.strip() for s in txt.splitlines() if s.strip()]

if st.button("Calculate"):
    rows, bad = [], []
    with st.spinner("Calculating…"):
        for s in lines:
            p = chem.properties(s)
            if p:
                rows.append(p)
            else:
                bad.append(s)
    if bad:
        st.warning(f"Skipped {len(bad)} invalid SMILES: {', '.join(bad[:5])}")
    if rows:
        df = pd.DataFrame(rows)
        if len(df) == 1:
            r = df.iloc[0]
            c = st.columns(4)
            for col, k in zip(c, ["MW", "LogP", "TPSA", "RotBonds"]):
                col.metric(k, r[k])
            c = st.columns(3)
            c[0].metric("HBD", int(r["HBD"]))
            c[1].metric("HBA", int(r["HBA"]))
            c[2].metric("Lipinski", "Pass ✅" if r["Passes Ro5"] else "Fail ❌", f'{r["Lipinski violations"]} violation(s)')
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button("Download CSV", df.to_csv(index=False), "properties.csv", "text/csv")
    elif not bad:
        st.info("Enter at least one SMILES.")
footer()
