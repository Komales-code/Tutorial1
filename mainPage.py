import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Resume | Komaleswari Deva", page_icon=":briefcase:", layout="wide")

# --- Custom CSS Styling (Dark Grey Compact) ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2C2C2C;
        color: #F5F5F5;
        font-family: "Arial", sans-serif;
        font-size: 14px;
    }

    h1 {
        color: #EAECEE;
        font-size: 28px !important;
        margin-bottom: 5px;
    }

    h2 {
        color: #4DB6AC;
        font-size: 18px !important;
        border-left: 5px solid #4DB6AC;
        padding-left: 8px;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    h3 {
        color: #AED6F1;
        font-size: 16px !important;
        margin-top: 8px;
    }

    .resume-box {
        padding: 8px;
        border-radius: 8px;
        background-color: #3A3A3A;
        margin-bottom: 12px;
        box-shadow: 0px 1px 4px rgba(0,0,0,0.4);
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
    }

    .stDownloadButton button {
        background-color: #4DB6AC;
        color: white;
        border-radius: 6px;
        padding: 6px 15px;
        border: none;
        font-size: 14px;
    }
    .stDownloadButton button:hover {
        background-color: #26A69A;
        color: #EAECEE;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header Section ---
col1, col2 = st.columns([1, 4], gap="small")
with col1:
    st.image("profile.jpg", width=150)  # Profile photo
with col2:
    st.title("Komaleswari Deva")
    st.write("💻 IT Student | Universiti Malaysia Kelantan")

st.markdown("---")

# --- Two Column Layout ---
left, right = st.columns(2, gap="large")

# -------- LEFT COLUMN --------
with left:
    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("👤 Personal Profile")
    st.write("**Age:** 23")
    st.write("**Date of Birth:** 13 / 06 / 2002")
    st.write("**Race/Religion:** Indian / Hindu")
    st.write("**Nationality:** Malaysian")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("📞 Contact")
    st.write("📧 **komales047@gmail.com**")
    st.write("📱 **+60 16-2309130**")
    st.write("🏠 No.9, Jalan Kemboja 6, Taman Aman, 42700 Banting, Selangor")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🛠 Skills")
    st.subheader("Technical Skills")
    st.write("- MS Office\n- VB Studio\n- Adobe Animate\n- HTML & CSS")
    st.subheader("Personal Attributes")
    st.write("- Fast learner\n- Active listener\n- Information literacy\n- Team player")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🌐 Languages")
    st.write("- English: Proficient\n- Malay: Proficient\n- Tamil: Native (Proficient)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🎯 Interests")
    st.write("Hiking | Running | Badminton | Travelling | Cooking")
    st.markdown('</div>', unsafe_allow_html=True)

# -------- RIGHT COLUMN --------
with right:
    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🎯 Career Objective")
    st.write(
        """
        Motivated and hardworking Information Technology student currently pursuing a Bachelor’s degree. Skilled in programming, database management, and web application development.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("**Bachelor of Information Technology (Hons.)** – Universiti Malaysia Kelantan (2023 – Present) | CGPA: 3.46")
    st.write("**Diploma in Information Technology** – Politeknik Seberang Perai (2021 – 2023) | CGPA: 3.81")
    st.write("**Sijil Pelajaran Malaysia (SPM)** – SMK Methodist Telok Datok (2019)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("💼 Work Experience")
    st.subheader("Trainee | Ibu Pejabat Daerah Kuala Langat (Jan 2023 – Jun 2023)")
    st.write("- Maintained details by entering new and updated case files.\n- Developed a system to update information.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🏆 Achievements")
    st.write("- Final Year Project: Physiotherapy Centre Web Application (HTML, CSS, PHP, JS, MySQL)")
    st.write("- Academic Excellence: Diploma CGPA 3.81")
    st.write("- Kabaddi Competition 2016 – 2nd Place")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("🤝 Co-Curricular & Leadership")
    st.write("**2024 | Fun Run (Sultan Selangor Birthday)** – Completed 6km run")
    st.write("**2024 | Aviraa 1.0 (UMK)** – Facilitator, assisted in event coordination")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("📞 Referees")
    st.write("**Ts. Dr. Nor Alina Binti Ismail** – Advisor, Universiti Malaysia Kelantan | 📱 +60 19-2200139")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-box">', unsafe_allow_html=True)
    st.header("📄 Resume PDF")
    if st.button("⬇️ Generate Resume PDF"):
        st.info("This is a placeholder button (no PDF generated yet).")
    st.markdown('</div>', unsafe_allow_html=True)
