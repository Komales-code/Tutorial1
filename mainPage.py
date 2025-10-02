import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #2C2C2C; 
        color: #F5F5F5;            
        font-family: "Arial", sans-serif;
    }

    h1 {
        color: #EAECEE;
        font-size: 42px !important;
    }

    h2 {
        color: #4DB6AC; 
        border-left: 6px solid #4DB6AC;
        padding-left: 10px;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    h3 {
        color: #AED6F1; 
        margin-top: 15px;
    }

    .resume-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #3A3A3A; 
        margin-bottom: 20px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.5);
    }

    .stDownloadButton button {
        background-color: #4DB6AC;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stDownloadButton button:hover {
        background-color: #26A69A;
        color: #EAECEE;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4], gap="small")

with col1:
    st.image("profile.jpg", width=180)

with col2:
    st.title("Komaleswari Deva")
    st.write("💻 IT Student | Universiti Malaysia Kelantan")
    st.write("📧 **komales047@gmail.com** | 📱 **+60 16-2309130**")
    st.write("🏠 No.9, Jalan Kemboja 6, Taman Aman, 42700 Banting, Selangor")
    st.markdown("---")

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🎯 Career Objective")
st.write(
    """
    Motivated and hardworking Information Technology student currently pursuing a Bachelor’s degree. Skilled in programming, database management, and web application development. Seeking opportunities to apply technical knowledge and interpersonal skills in real-world IT projects while continuously learning and contributing to organizational success.
    """
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🎓 Education")
st.write("**Bachelor of Information Technology (Hons.)** – Universiti Malaysia Kelantan (2023 – Present) | Current CGPA: 3.46")
st.write("**Diploma in Information Technology** – Politeknik Seberang Perai (2021 – 2023) | CGPA: 3.81")
st.write("**Sijil Pelajaran Malaysia (SPM)** – SMK Methodist Telok Datok (2019)")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("💼 Work Experience")
st.subheader("Trainee | Ibu Pejabat Daerah Kuala Langat (Jan 2023 – Jun 2023)")
st.write(
    """
    - Maintained details by entering new and updated case files.  
    - Developed a system to update information.  
    """
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🛠 Skills")

st.subheader("Technical Skills")
col1, col2= st.columns(2)

with col1:
    st.write("- MS Office")
    st.write("- VB Studio")
    st.write("- Adobe Animate")

with col2:
    st.write("- Python")
    st.write("- Android Studio")
    st.write("- GUI Programming")

st.subheader("Personal Attributes")
col3, col4 = st.columns(2)

with col3:
    st.write("- Fast Learner")
    st.write("- Active Listener")
    st.write("- Information Literacy")

with col4:
    st.write("- Team Player")
    st.write("- Innovative")
    st.write("- Easy Adaptability")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🌐 Languages")
st.write("- English: Proficient")
st.write("- Malay: Proficient")
st.write("- Tamil: Native (Proficient)")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🏆 Achievements")
st.write("**Final Year Project (Diploma)** – Developed a Physiotherapy Centre Web Application using HTML, CSS, PHP, JS, MySQL")
st.write("**Academic Excellence** – Diploma CGPA: 3.81")
st.write("**Kabaddi Competition 2016** – 2nd Place")
st.write("**Short Story Writing Competition 2018** – Consolation Prize")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🤝 Co-Curricular & Leadership Activities")
st.write("**2024 | Fun Run (Sultan Selangor Birthday)** – Completed 6km run")
st.write("**2024 | Aviraa 1.0 (UMK)** – Facilitator, assisted in event coordination")
st.write("**2019 | Kabaddi Club (SMK Methodist Telok Datok)** – Vice Secretary, managed meetings & correspondence")
st.write("**2019 | Girl Squad (SMK Methodist Telok Datok)** – Secretary, organized meetings & administration")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("🎯 Interests")
st.write("Hiking | Running | Badminton | Travelling | Cooking")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("📞 Referees")
st.write("**Ts. Dr. Nor Alina Binti Ismail** – Advisor, University Malaysia Kelantan | 📱 +60 19-2200139")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="resume-box">', unsafe_allow_html=True)
st.header("📄 Resume PDF")

st.markdown('</div>', unsafe_allow_html=True)
