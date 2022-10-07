from pathlib import Path
import streamlit as st
from PIL import Image
from st_functions import st_button, load_css
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1663725143084-29134fa3c18d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DHRUV TYAGI.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
#PAGE_TITLE = "PORTFOLIO | DHRUV TYAGI"
#PAGE_ICON = "🚀"
NAME = "DHRUV TYAGI"
EMAIL = "dhruvtyagionly1@gmail.com"

#st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

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

st.header("DHRUV  TYAGI")

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
with cola:
  st.write('')
with colb:
  st.subheader("PROJECTS")
with colc:
  st.write('')

st.image("https://i.pinimg.com/originals/e5/93/ab/e593ab0589d5f1b389e4dfbcce2bce20.gif")


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
st.image("https://static.wixstatic.com/media/614445_94fc54c7e5914b70a12a6ebcaebbde31~mv2.gif")

st_button('', 'https://github.com/Dhruv-0001/Tech_Article-NDB.git', 'NDBs', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Metaverse.git', 'METAVERSE', icon_size)


st.write('\n')
st.image("https://www.learninglinksindia.org/public/images/Journey-Boat.gif")
st.write('\n')

st.header("WORK EXPERIENCE")
st.write("\n")
st.header("INVARIANCE AUTOMATION LTD. | SDE Intern | Nov 2022 - Dec 2022 | IIT Kanpur")
st.markdown('''

-  To Develop an OpenCV and Python based User Interface which ensures the proper alignment of various components on PCB.
-  To implement machine learning models for matching the product with the prototype for building an automated PCB assembly line.
''')
st.header("SIEMENS | Research and Development Intern | June 2022 - August 2022 | Kalwa,Mumbai")
st.markdown('''
-  Created a workplan for the Automation of labs. In this an API of labs was created using Mind Connect IOT module.
-  Made a prototype application on Mindsphere cloud using Mendix and did PLC programming of labs on LOGO and TIA portal software
''')
st.write("\n")
st.image("https://media2.giphy.com/media/Sx9icPlpIAYSJiMYik/giphy.gif?cid=ecf05e475jqzcaep3a3svn4ecebs6kmrcls2a7isaatkj6d8&rid=giphy.gif&ct=s")

st.header("EXTRA-CURRICULAR")
st.write("\n")
st.subheader("SIEMENS SCHOLAR")
st.markdown('''
-  I am honored to be selected as a Siemens Scholar.
-  In this, only the top 200 candidates from India are selected for the Germandual education-based Scholarship program.
''')
st.subheader("CO-SECRETARY, ALUMNI ASSOCIATION HBTU")
st.markdown('''
-  Organized and Managed Alumni Meet with Mr.President as our chief guest on the centennial celebration of HBTU.
-  Working on Building a Job Portal which will provide placement and internship opportunities to students.
''')
st.subheader("TECHNICAL WRITING")
st.markdown('''
-  Written some articles on Emerging Technologies including Nano Diamond Batteries,Metaverse,etc.
''')
st.subheader("SOCIAL MEDIA MANAGEMENT")
st.markdown('''
-  HANDLED THE INSTAGRAM PAGE OF ALUMNI ASSOCIATION AND LINKEDIN PAGE OF VARIOUS COLLEGE SOCITIES.
-  HAVE KNOWLEDGE OF SOCIAL MEDIA ALGORITHMS AND SEO.
''')
st.subheader("ATHLETICS")
st.markdown('''
-  WON MEDAL IN SPRINTING IN STATE CAMP.
-  LOVES TO WORKOUT, FOR BEING HEALTHY.
''')

st.image("https://media2.giphy.com/media/eNvPo1OAXVpZsSIUXU/200.gif?cid=82a1493bisbxsid6z8xkcqxn0ej4mq2vczxypcost3v019oc&rid=200.gif&ct=s")

