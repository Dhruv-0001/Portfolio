from pathlib import Path
import streamlit as st
from PIL import Image
from st_functions import st_button, load_css
import time
import requests

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DHRUV TYAGI.pdf"
profile_pic = current_dir / "assets" / "profile-pic (6).png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "DHRUV TYAGI | PORTFOLIO"
PAGE_ICON = "🚀"
NAME = "DHRUV TYAGI"
EMAIL = "dhruvtyagionly1@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
#with open(css_file) as f:
#    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(profile_pic)

st.header("DHRUV  TYAGI")

music("data:image/jpeg;base64,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","https://www.youtube.com/watch?v=kVpv8-5XWOI","LISTEN TO THIS BEAUTIFUL SONG 🎸")

cola,colb,colc=st.columns(3)
with colb:
    if st.button("▶ PLAY 🎸🎼 "):
        st.video("https://www.youtube.com/watch?v=kVpv8-5XWOI")

st.info("(●'◡'●)....Hello..! I am Just an avid learner who loves to apply Python and Machine learning on real world projects. I am currently deep diving into Data Science and have a keen interest in Blockchain and WEB 3.0 technologies🚀.")

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

st.image("https://cliply.co/wp-content/uploads/2019/12/371903520_SOCIAL_ICONS_TRANSPARENT_400px.gif")

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/dhruv-tyagi-9a526b218/', 'LINKEDIN', icon_size)
st_button('github', 'https://github.com/Dhruv-0001', 'GITHUB', icon_size)
st_button('instagram', 'https://www.instagram.com/iamdhruv.tyagi/', 'INSTAGRAM', icon_size)

st.write('\n')
cola,colb,colc = st.columns(3)
with colb:
  st.subheader("PROJECTS")

st.image("https://i.pinimg.com/originals/e5/93/ab/e593ab0589d5f1b389e4dfbcce2bce20.gif")

st_button('', 'https://dhruv-0001-shoe-hype-shoe-hype-8ebvwa.streamlitapp.com/', 'SHOE HYPE〽️', icon_size)
st_button('', 'https://dhruv-0001-stocks-forecastor-app-gqlm6j.streamlitapp.com/', 'STOCKS FORECASTER💹' , icon_size)
st_button('', 'https://github.com/Dhruv-0001/POSE_DETECTION', 'POSE DETECTION', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Reimagined-System', 'REIMAGINED SYSTEM', icon_size)

st.write('\n')
cola1,colb1,colc1 = st.columns(3)
with colb1:
  st.subheader("TECH ARTICLES")

st.write('\n')
st.image("https://static.wixstatic.com/media/614445_94fc54c7e5914b70a12a6ebcaebbde31~mv2.gif")

st_button('', 'https://github.com/Dhruv-0001/Tech_Article-NDB.git', 'NDBs', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Metaverse.git', 'METAVERSE', icon_size)
st.write('\n')

st.header("WORK EXPERIENCE")

st.write('\n')
st.image("https://www.learninglinksindia.org/public/images/Journey-Boat.gif")
st.write("\n")
st.header("INVARIANCE AUTOMATION LTD. | SDE Intern | Nov 2022 - Dec 2022 | IIT Kanpur")
st.markdown('▢ To Develop an OpenCV and Python based User Interface which ensures the proper alignment of various components on PCB.')
st.markdown('▢ To implement machine learning models for matching the product with the prototype for building an automated PCB assembly line.')
st.header("SIEMENS | Research and Development Intern | June 2022 - August 2022 | Kalwa,Mumbai")
st.markdown('▢ Created a workplan for the Automation of labs. In this an API of labs was created using Mind Connect IOT module.')
st.markdown('▢ Made a prototype application on Mindsphere cloud using Mendix and did PLC programming of labs on LOGO and TIA portal software')

st.header("EXTRA-CURRICULAR")
st.write("\n")
st.image("https://media2.giphy.com/media/Sx9icPlpIAYSJiMYik/giphy.gif?cid=ecf05e475jqzcaep3a3svn4ecebs6kmrcls2a7isaatkj6d8&rid=giphy.gif&ct=s")
st.write("\n")

st.subheader("SIEMENS SCHOLAR")
st.markdown('▢ I am honored to be selected as a Siemens Scholar.')
st.markdown('▢ In this, only the top 200 candidates from India are selected for the Germandual education-based Scholarship program.')
st.subheader("CO-SECRETARY, ALUMNI ASSOCIATION HBTU")
st.markdown('▢ Organized and Managed Alumni Meet with Mr.President as our chief guest on the centennial celebration of HBTU.')
st.markdown('▢ Working on Building a Job Portal which will provide placement and internship opportunities to students.')
st.subheader("TECHNICAL WRITING")
st.markdown('▢ Written some articles on Emerging Technologies including Nano Diamond Batteries,Metaverse,etc.')
st.subheader("SOCIAL MEDIA MANAGEMENT")
st.markdown('▢ HANDLED THE INSTAGRAM PAGE OF ALUMNI ASSOCIATION AND LINKEDIN PAGE OF VARIOUS COLLEGE SOCITIES.')
st.markdown('▢ HAVE KNOWLEDGE OF SOCIAL MEDIA ALGORITHMS AND SEO.')
st.subheader("ATHLETICS")
st.markdown('▢ WON MEDAL IN SPRINTING IN STATE CAMP.')
st.markdown('▢ LOVES TO WORKOUT, FOR BEING HEALTHY.')

st.image("https://i.gifer.com/50Tg.gif")

