from pathlib import Path
import streamlit as st
from PIL import Image
from st_functions import *
import time
import requests
import streamlit.components.v1 as components

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DHRUV_TYAGI.pdf"
profile_pic = current_dir / "assets" / "profile-pic (6).png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "DhruvCodes | PORTFOLIO"
#PAGE_ICON = "🚀"
NAME = "DHRUV TYAGI"
EMAIL = "dhruvtyagionly1@gmail.com"

st.set_page_config(page_title=PAGE_TITLE)
icon_size = 20

with st.sidebar:
        components.html(embed_component['linkedin'],height=310)
        st_button('', 'https://www.buymeacoffee.com/DhruvTyagi', 'Buy Me a Coffee☕', icon_size)
        st_button('', 'https://drive.google.com/file/d/1kbYbeIgRGAe0Qzx3px0a9hb3muQcudFI/view?usp=share_link', 'Download Resume', icon_size)

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

cola,colb,colc=st.columns(3)
with colb:
    if st.button("Listen A Melody 🎸 "):
        st.video("https://www.youtube.com/watch?v=syFZfO_wfMQ")

st.info("I am Just an avid learner who loves to apply Python and Machine learning on real world problems. I am currently deep diving into Data Science, Open Source and have a keen interest in Blockchain and WEB 3.0 technologies🚀.")

st.image("https://cliply.co/wp-content/uploads/2019/12/371903520_SOCIAL_ICONS_TRANSPARENT_400px.gif")

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/dhruv-tyagi-9a526b218/', 'LINKEDIN', icon_size)
st_button('github', 'https://github.com/Dhruv-0001', 'GITHUB', icon_size)
st_button('instagram', 'https://www.instagram.com/iamdhruv.tyagi/', 'INSTAGRAM', icon_size)
st_button('', 'https://mail.google.com/mail/?view=cm&source=mailto&to=dhruvtyagionly1@gmail.com', 'dhruvtyagionly1@gmail.com', icon_size)

st.write('\n')
cola,colb,colc = st.columns(3)
with colb:
  st.subheader("PROJECTS")

st.image("https://i.pinimg.com/originals/e5/93/ab/e593ab0589d5f1b389e4dfbcce2bce20.gif")

st_button('', 'https://dhruv-0001-shoe-hype-shoe-hype-8ebvwa.streamlitapp.com/', 'SHOE HYPE〽️', icon_size)
st_button('', 'https://dhruv-0001-snapshot-app-keifr6.streamlit.app/', 'Snap Shot', icon_size)
st_button('', 'https://dhruv-0001-hacktoberfest2022-tech-talk-main-z5l9tc.streamlit.app/', 'TECH TALK', icon_size)
st_button('', 'https://dhruv-0001-stocks-forecastor-app-gqlm6j.streamlitapp.com/', 'STOCKS FORECASTER💹' , icon_size)
st_button('', 'https://github.com/Dhruv-0001/POSE_DETECTION', 'POSE DETECTION', icon_size)

nu=["cola1","colb1","colc1"]        
nu = st.columns(3)
with nu[1]:
  st.subheader("TECH ARTICLES")

st.write('\n')
st.image("https://static.wixstatic.com/media/614445_94fc54c7e5914b70a12a6ebcaebbde31~mv2.gif")
st.markdown('•  Written some articles on Emerging Technologies including Nano Diamond Batteries,Metaverse,etc.')
st_button('', 'https://github.com/Dhruv-0001/Tech_Article-NDB.git', 'NDBs', icon_size)
st_button('', 'https://github.com/Dhruv-0001/Metaverse.git', 'METAVERSE', icon_size)
st.write('\n')

st.header("WORK EXPERIENCE")

st.write('\n')
st.image("https://www.learninglinksindia.org/public/images/Journey-Boat.gif")
st.write("\n")
st.header("SIEMENS")
st.subheader("Research and Development Intern")
st.markdown('• Researched and created the work plan for the Automation of Lab work at the R&D department.')
st.markdown('• Created API of labs using the Mind Connect IOT 2040 module for controlling the labs remotely.')
st.markdown('• Prototyped an application on Mindsphere cloud using Mendix and designed PLC programs of 10+ labs on LOGO and TIA software.')
st_button('', 'https://github.com/Dhruv-0001/Reimagined-System', 'REIMAGINED SYSTEM', icon_size)

st.write("\n")

st.header("Open-Source Maintainer")
st.subheader("Hacktoberfest")
st.markdown('• Maintained and developed the Tech Talk (An Open-Source Tech Topics Learning Website) at Hacktoberfest 2022.')
st_button('', 'https://dhruv-0001-hacktoberfest2022-tech-talk-main-z5l9tc.streamlit.app/', 'TECH TALK', icon_size)

st.write("\n")

st.header("Research Work")
st.subheader("Real Time Recommendation Engine for Social Media Awareness")
st.markdown('Currently Ongoing')
st.markdown('• A real time Recommendation Engine which provides updates, resources, news articles, sentimental analysis, etc. on trending\latest topics surfing on social media.')

st.write("\n")

st.header("Skills & Tools")
st.image("https://spansystech.com/images/hero/banner3.gif")
st.write("\n")
skills=["• Python","• NumPy","• Pandas","• Matplotlib","• NLP","• SQL","• Shell Scripting","• Data Analysis","• Data Visualization", "• Data Modeling", "• Deployment", "• Deep Learning","• Django","• Apache","• Git", "• Data Structures", "• Algorithms", "• Statistics", "• DBMS", "• Excel", "• Linux/Ubuntu","• Streamlit"]

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[0])
with colb:
        st.markdown(skills[1])
with colc:
        st.markdown(skills[2])
with cold:
        st.markdown(skills[3])
st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[4])
with colb:
        st.markdown(skills[5])
with colc:
        st.markdown(skills[6])
with cold:
        st.markdown(skills[7])

st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[8])
with colb:
        st.markdown(skills[9])
with colc:
        st.markdown(skills[10])
with cold:
        st.markdown(skills[11])

st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[12])
with colb:
        st.markdown(skills[13])
with colc:
        st.markdown(skills[14])
with cold:
        st.markdown(skills[15])

st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[16])
with colb:
        st.markdown(skills[17])
with colc:
        st.markdown(skills[21])
with cold:
        st.markdown(skills[19])
        
st.write("\n")

cola,colb,colc,cold=st.columns(4)
with colb:
        st.markdown(skills[20])
with colc:
        st.markdown(skills[18])
        
st.write('\n')
st.header("ACHIEVEMENTS")
st.write("\n")
st.image("https://cliply.co/wp-content/uploads/2021/02/392102940_MEDAL_3D_400px.gif")
st.write("\n")

st.subheader("SIEMENS SCHOLAR")
st.markdown('•  I am honored to be selected as a Siemens Scholar.')
st.markdown('•  In this, only the top 200 candidates from India are selected for the Germandual education-based Scholarship program.')
st_button('', 'https://new.siemens.com/in/en/company/sustainability/corporate-citizenship/siemens-scholarship-program.html', 'KNOW MORE!', icon_size)
st.subheader("BERTELSMANN SSHOLAR")
st.markdown('• Selected as the recipient of Bertelsmann Scholarship for Data Science with Python Nano degree program via Udacity.')
st.subheader("HACKERRANK CERTIFICATION")
st.markdown('• Cleared the Python HackerRank and SQL (Intermediate) HackerRank Certification Test.')
st_button('', 'https://www.hackerrank.com/certificates/deeaa1a5369f', 'CERTIFICARE 1', icon_size)
st_button('', 'https://www.hackerrank.com/certificates/e923aeac56ea', 'CERTIFICARE 2', icon_size)
st.subheader("MECHATRONICS TRAINING")
st.markdown('• Awarded Mechatronics Level 1 & 2 (Learnt PLC programming) and soft skills Training by Growth Center.')

st.write("\n")
st.header("EXTRA-CURRICULAR")
st.write("\n")
st.image("https://images.squarespace-cdn.com/content/v1/59d22f80f14aa1300681d5d6/1592228025808-EXNM0WEGVPOAN0KK6ZJI/colgatehat-2.gif?format=500w")
st.write("\n")

st.subheader("CO-SECRETARY, ALUMNI ASSOCIATION HBTU")
st.markdown('•  Organized and Managed Alumni Meet with Mr.President as our chief guest on the centennial celebration of HBTU.')
st.subheader("HBTU UNSTOP IGNITERS CLUB")
st.markdown('•  Conduct various National level events in HBTU that gave students exposure to compete and show their skills at a big stage.')
st.subheader("SOCIAL MEDIA MANAGEMENT")
st.markdown('•  HANDLED THE INSTAGRAM PAGE OF ALUMNI ASSOCIATION AND LINKEDIN PAGE OF VARIOUS COLLEGE SOCIETIES.')
st.markdown('•  HAVE KNOWLEDGE OF SOCIAL MEDIA ALGORITHMS AND SEO.')
st.subheader("ATHLETICS")
st.markdown('•  WON MEDAL IN SPRINTING IN STATE CAMP.')

st.image("https://i.gifer.com/50Tg.gif")

