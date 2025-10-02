import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Resume | Your Name", page_icon=":briefcase:", layout="wide")

# --- Hero Section ---
col1, col2 = st.columns([1, 4], gap="small")

with col1:
    st.image("profile.jpeg", width=180)  # Your profile photo

with col2:
    st.title("Your Full Name")
    st.write("💼 Job Title | 🎓 Degree | 🌍 Location")
    st.write("📧 your.email@example.com | 📱 +60-123-456-789 | 🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | 🐙 [GitHub](https://github.com/yourusername)")
    st.markdown("---")

# --- Summary ---
st.subheader("👋 Summary")
st.write(
    """
    Motivated and detail-oriented professional with experience in **software development, data analysis, and project management**. 
    Skilled at building web apps, visualizing data, and solving complex problems with creative solutions.
    """
)
st.markdown("---")

# --- Education ---
st.subheader("🎓 Education")
st.write("**Bachelor of Computer Science** – University Name (2021 - 2025)")
st.write("Relevant Coursework: Data Structures, AI, Database Systems, Software Engineering")
st.markdown("---")

# --- Experience ---
st.subheader("💼 Work Experience")

st.markdown("**Software Intern | Tech Company** (Jun 2024 – Aug 2024)")
st.write(
    """
    - Built a customer dashboard using Streamlit & Python  
    - Automated reporting system with Pandas & Excel, reducing manual work by 40%  
    - Collaborated with a 5-member team in an Agile environment  
    """
)

st.markdown("**Freelance Web Developer** (2023 – Present)")
st.write(
    """
    - Designed and deployed responsive websites for 4+ small businesses  
    - Implemented online booking and e-commerce features using Django & Firebase  
    """
)
st.markdown("---")

# --- Skills ---
st.subheader("🛠 Skills")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("- Python")
    st.write("- SQL")
    st.write("- Streamlit")
with col2:
    st.write("- Git/GitHub")
    st.write("- HTML/CSS/JS")
    st.write("- Flask/Django")
with col3:
    st.write("- Data Visualization")
    st.write("- Problem Solving")
    st.write("- Communication")
st.markdown("---")

# --- Projects ---
st.subheader("📂 Projects")

st.markdown("**Personal Portfolio Website** – Built with Streamlit, deployed on Streamlit Cloud")
st.markdown("**Data Analysis Dashboard** – Interactive sales analytics dashboard with Pandas & Matplotlib")
st.markdown("**Mobile App (Team Project)** – Professor Appointment Booking App using Flutter & Firebase")
st.markdown("---")

# --- Achievements ---
st.subheader("🏆 Achievements")
st.write("- Dean’s List (2022, 2023)")
st.write("- Hackathon Winner 2024 – Built AI-powered study assistant")
st.write("- Certified in Google Data Analytics (2025)")
st.markdown("---")

# --- Download Resume Button ---
with open("resume.pdf", "rb") as file:
    st.download_button("📄 Download My Resume", file, "resume.pdf", mime="application/pdf")
