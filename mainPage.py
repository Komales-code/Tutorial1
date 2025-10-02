import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Resume | Komaleswari Deva", page_icon=":briefcase:", layout="wide")

# --- Hero Section ---
col1, col2 = st.columns([1, 4], gap="small")

with col1:
    st.image("profile.jpg", width=180)  # Replace with your profile photo (JPEG/PNG)

with col2:
    st.title("Komaleswari Deva")
    st.write("💻 IT Student | Universiti Malaysia Kelantan")
    st.write("📧 komales047@gmail.com | 📱 +60 16-2309130")
    st.write("🏠 No.9, Jalan Kemboja 6, Taman Aman, 42700 Banting, Selangor")
    st.markdown("---")

# --- Career Objective ---
st.subheader("🎯 Career Objective")
st.write(
    """
    Motivated and hardworking Information Technology student currently pursuing a Bachelor’s degree.  
    Skilled in programming, database management, and web application development.  
    Seeking opportunities to apply technical knowledge and interpersonal skills in real-world IT projects 
    while continuously learning and contributing to organizational success.
    """
)
st.markdown("---")

# --- Education ---
st.subheader("🎓 Education")
st.write("**Bachelor of Information Technology (Hons.)**, Universiti Malaysia Kelantan (2023 – Present) | Current CGPA: 3.46")
st.write("**Diploma in Information Technology**, Politeknik Seberang Perai (2021 – 2023) | CGPA: 3.81")
st.write("**Sijil Pelajaran Malaysia (SPM)**, SMK Methodist Telok Datok (2019)")
st.markdown("---")

# --- Work Experience ---
st.subheader("💼 Work Experience")
st.markdown("**Trainee | Ibu Pejabat Daerah Kuala Langat** (Jan 2023 – Jun 2023)")
st.write(
    """
    - Maintained details by entering new and updated case files.  
    - Developed a system to update information.  
    """
)
st.markdown("---")

# --- Skills ---
st.subheader("🛠 Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("- MS Office")
    st.write("- VB Studio")
    st.write("- Adobe Animate")
with col2:
    st.write("- HTML & CSS")
    st.write("- PHP")
    st.write("- Java")
with col3:
    st.write("- Python")
    st.write("- Android Studio")
    st.write("- GUI Programming")

st.subheader("🌟 Personal Attributes")
st.write(
    """
    - Fast learner  
    - Active listener  
    - Information literacy  
    - Team player  
    - Innovative  
    - Easy adaptability  
    - Positive attitude  
    """
)
st.markdown("---")

# --- Languages ---
st.subheader("🌐 Languages")
st.write("- English: Proficient")
st.write("- Malay: Proficient")
st.write("- Tamil: Native (Proficient)")
st.markdown("---")

# --- Achievements ---
st.subheader("🏆 Achievements")
st.write("**Final Year Project (Diploma)** – Developed a Physiotherapy Centre Web Application using HTML, CSS, PHP, JS, MySQL")
st.write("**Academic Excellence** – Diploma CGPA: 3.81")
st.write("**Kabaddi Competition 2016** – 2nd Place")
st.write("**Short Story Writing Competition 2018** – Consolation Prize")
st.markdown("---")

# --- Co-curricular & Leadership ---
st.subheader("🤝 Co-Curricular & Leadership Activities")
st.write("**2024 | Fun Run (Sultan Selangor Birthday)** – Completed 6km run")
st.write("**2024 | Aviraa 1.0 (UMK)** – Facilitator, assisted in event coordination")
st.write("**2019 | Kabaddi Club (SMK Methodist Telok Datok)** – Vice Secretary, managed meetings & correspondence")
st.write("**2019 | Girl Squad (SMK Methodist Telok Datok)** – Secretary, organized meetings & administration")
st.markdown("---")

# --- Interests ---
st.subheader("🎯 Interests")
st.write("Hiking | Running | Badminton | Travelling | Cooking")
st.markdown("---")

# --- Referees ---
st.subheader("📞 Referees")
st.write("**Ts. Dr. Nor Alina Binti Ismail** – Advisor, University Malaysia Kelantan | 📱 +60 19-2200139")

# --- Download Resume Button ---
with open("KOMALESWARI DEVA.pdf", "rb") as pdf_file:
    st.download_button("📄 Download My Resume (PDF)", pdf_file, "Komaleswari_Deva_Resume.pdf", mime="application/pdf")
