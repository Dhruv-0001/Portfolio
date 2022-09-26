from pathlib import Path
import streamlit as st
from PIL import Image
from st_functions import st_button, load_css
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DHRUV TYAGI.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "PORTFOLIO | DHRUV TYAGI"
PAGE_ICON = ":wave:"
NAME = "DHRUV TYAGI"
EMAIL = "dhruvtyagionly1@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
#with open(css_file) as f:
#    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#lootieS
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(profile_pic)

st.header('DHRUV TYAGI')

st.info("(●'◡'●)....Hello..! I am Just an avid learner interested in real life applications of Python and Machine learning. I have a keen interest in Blockchain and WEB 3.0 technologies.")

col19,col20 = st.columns(2)
with col19 :
  st.download_button(
      label=" 📄 Download Resume",
      data=PDFbyte,
      file_name=resume_file.name,
      mime="application/octet-stream",
  )
with col20 :
  st.write("📫", EMAIL)

st.write('\n')
cola2,colb2,colc2 = st.columns(3)
with cola2:
  st.write('')
with colb2:
  lottie_url_hello = "https://assets3.lottiefiles.com/packages/lf20_nfr0ytlp.json"
  lottie_hello = load_lottieurl(lottie_url_hello)
  st_lottie(lottie_hello)
with colc2:
  st.write('')


icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/dhruv-tyagi-9a526b218/', 'LINKEDIN', icon_size)
st_button('', 'https://github.com/Dhruv-0001', 'GITHUB', icon_size)
st_button('', 'https://www.instagram.com/iamdhruv.tyagi/', 'INSTAGRAM', icon_size)

st.write('\n')
cola,colb,colc = st.columns(3)
with cola:
  st.write('')
with colb:
  st.subheader("PROJECTS")
with colc:
  st.write('')

st.write('\n')
cola2,colb2,colc2 = st.columns(3)
with cola2:
  st.write('')
with colb2:
  lottie_url_hello = "https://assets7.lottiefiles.com/packages/lf20_ygiuluqn.json"
  lottie_hello = load_lottieurl(lottie_url_hello)
  st_lottie(lottie_hello)
with colc2:
  st.write('')

st_button('', 'https://dhruv-0001-shoe-hype-shoe-hype-8ebvwa.streamlitapp.com/', 'SHOE HYPE〽️', icon_size)
st_button('', 'https://github.com/Dhruv-0001/POSE_DETECTION', 'POSE DETECTION', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Reimagined-System', 'REIMAGINED SYSTEM', icon_size)

st.write('\n')
cola1,colb1,colc1 = st.columns(3)
with cola1:
  st.write('')
with colb1:
  st.subheader("TECH ARTICLES")
with colc1:
  st.write('')

st.write('\n')
cola2,colb2,colc2 = st.columns(3)
with cola2:
  st.write('')
with colb2:
  lottie_url_hello = "https://assets10.lottiefiles.com/packages/lf20_dwmb4mrt.json"
  lottie_hello = load_lottieurl(lottie_url_hello)
  st_lottie(lottie_hello)
with colc2:
  st.write('')

st_button('', 'https://github.com/Dhruv-0001/Tech_Article-NDB.git', 'NDBs', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Metaverse.git', 'METAVERSE', icon_size)


st.write('\n')
cola2,colb2,colc2 = st.columns(3)
with cola2:
  st.write('')
with colb2:
  lottie_url_hello = "https://assets3.lottiefiles.com/private_files/lf30_vc1vwgxh.json"
  lottie_hello = load_lottieurl(lottie_url_hello)
  st_lottie(lottie_hello)
with colc2:
  st.write('')

st.write('\n')
cola11,colb11,colc11 = st.columns(3)
with cola11:
  st.write('')
with colb11:
  st.subheader("KNOW MORE")
with colc11:
  st.write('')


st.write('\n')

col22,col8,col23 = st.columns(3)
with col22:
  if st.button("WORK EXPERIENCE"): 
    st.write("hi2")
with col8:
  st.write("")
with col23:
  if st.button("EXTRA-CURRICULAR"):
    st.write("hi3")

lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_x62chJ.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

