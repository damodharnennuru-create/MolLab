import streamlit as st

FOOTER_TEXT = "Created by Nennuru Damodhar Reddy | RA2611026050176 | Section: AIML C"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], .stApp {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Helvetica Neue", sans-serif;
  color: #1D1D1F; background: #FBFBFD;
}
header[data-testid="stHeader"] {
  background: rgba(251,251,253,.72); backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px); border-bottom: 1px solid #D2D2D7;
}
#MainMenu, footer {visibility: hidden;}
.block-container {max-width: 1100px; padding-top: 3rem; padding-bottom: 2rem;}
section[data-testid="stSidebar"] {background: #FFFFFF; border-right: 1px solid #D2D2D7;}
h1, h2, h3 {letter-spacing: -0.02em; font-weight: 700; color: #1D1D1F;}
.hero {text-align: center; padding: 3.5rem 1rem 2.5rem;}
.hero h1 {font-size: clamp(2.4rem, 6vw, 4.2rem); font-weight: 800; line-height: 1.05; margin: 0 0 .8rem;}
.hero p {font-size: clamp(1.05rem, 2vw, 1.4rem); color: #6E6E73; max-width: 680px; margin: 0 auto;}
.card-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 1.5rem 0;}
.card {background: #FFFFFF; border: 1px solid #D2D2D7; border-radius: 18px; padding: 1.6rem;
  box-shadow: 0 2px 12px rgba(0,0,0,.04); transition: transform .25s ease, box-shadow .25s ease;}
.card:hover {transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,.10);}
.card .icon {font-size: 2rem;} .card h3 {margin: .6rem 0 .3rem; font-size: 1.25rem;}
.card p {color: #6E6E73; margin: 0; font-size: .95rem; line-height: 1.45;}
.stButton > button, .stDownloadButton > button {
  border-radius: 980px; background: #0071E3; color: #fff; border: none; padding: .55rem 1.4rem;
  font-weight: 500; transition: all .2s ease;}
.stButton > button:hover, .stDownloadButton > button:hover {background: #0077ED; color: #fff; transform: scale(1.02);}
.stTextInput input, .stTextArea textarea, .stNumberInput input {border-radius: 12px !important; border: 1px solid #D2D2D7 !important;}
div[data-baseweb="tab-list"] {gap: 4px; background: #EDEDF0; padding: 4px; border-radius: 12px; width: fit-content;}
button[data-baseweb="tab"] {border-radius: 9px; padding: .3rem 1rem;}
div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] {display: none;}
button[data-baseweb="tab"][aria-selected="true"] {background: #FFFFFF; box-shadow: 0 1px 4px rgba(0,0,0,.12);}
[data-testid="stMetric"] {background: #fff; border: 1px solid #D2D2D7; border-radius: 16px; padding: 1rem 1.2rem;}
[data-testid="stMetricLabel"] {color: #6E6E73;}
.mol-box {background: #fff; border: 1px solid #D2D2D7; border-radius: 18px; padding: 1rem; text-align: center;}
.app-footer {margin-top: 4rem; padding: 1.2rem 0 .5rem; border-top: 1px solid #D2D2D7;
  text-align: center; color: #6E6E73; font-size: .8rem;}
</style>
"""

def setup(title, icon="🧪"):
    st.set_page_config(page_title=f"{title} · Cheminformatics Virtual Lab", page_icon=icon, layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)

def hero(title, subtitle):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)

def footer():
    st.markdown(f'<div class="app-footer">{FOOTER_TEXT}</div>', unsafe_allow_html=True)
