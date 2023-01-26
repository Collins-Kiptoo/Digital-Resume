from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "PIC.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Collins Kiptoo Kiprotich"
PAGE_ICON = ":wave:"
NAME = "Collins Kiptoo Kiprotich"
DESCRIPTION = """
Data Scientist, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "collinskip10@gmail.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/collins-kiprotich-b2806a101",
    "GitHub": "https://github.com/Collins-Kiptoo",
    "Kaggle": "https://www.kaggle.com/collinskkiprotich",
}
PROJECTS = {
    "🏆 Box Office Hits Prediction": "https://github.com/Collins-Kiptoo/dsc-phase-1-project-v2-4",
    "🏆 House Prediction Analysis": "https://github.com/Collins-Kiptoo/dsc-phase-2-project-v2-3",
    "🏆 Telecom Customer Churn Prediction": "https://github.com/Collins-Kiptoo/Telecom-Customer-Churn-Prediction",
    "🏆 Anime Recommendation System ": "https://github.com/Collins-Kiptoo/Movie-Recommendation-System",
    "🏆 Alzheimer's Disease Detection ": "https://github.com/Collins-Kiptoo/Alzheimer-s-Disease-Detection",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Experience working remotely and online
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: Tableau, PowerBi, Matplotlib, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decision trees, CNN
- 🗄️ Databases: MongoDB, SQLite, MySQL

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scoper | [Invisible Technologies, Inc](https://www.invisible.co/)**")
st.write("02/2021 - Present")
st.write(
    """
- ► Proven track record of success in data entry and team collaboration roles.
- ► Demonstrated ability to accurately and efficiently enter large amounts of data, ensuring that all information is accurate and up-to-date.
- ► Strong ability to work effectively in a team environment, collaborating with other team members to ensure that client needs are met on time and to the highest standard.
- ► Adept at multitasking and prioritizing competing demands, able to meet tight deadlines while maintaining a high level of attention to detail.
- ► Excellent communication and interpersonal skills, able to communicate effectively with clients and internal teams to deliver results.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Website Tester | [FitsWarm](https://www.linkedin.com/company/fitswarm-ltd./)**")
st.write("08/2020 - 08/2022")
st.write(
    """
- ► Collaborated with the product management to design, build and test systems.
- ► Conducted regression testing, analyze results and submit observations to the development team.
- ► Effectively interacted with the project manager regarding software defects and functionality issues, working closely to develop innovative solutions.
- ► Identified and tracked defects with Trello and supported developers in resolving problems by completing additional tests.
- ► Evaluated function, performance and design compliance of every product against design standards and customer needs.
""")





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
