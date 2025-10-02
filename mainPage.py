import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="My Resume", page_icon=":briefcase:", layout="wide")

# --- Profile Picture and Name ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpg", width=150)  # Replace with your photo file

with col2:
    st.title("Your Full Name")
    st.write("📧 your.email@example.com | 📱 (123) 456-7890 | 🌐 [LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("💼 Short tagline or summary about you (e.g., Data Analyst | Python Developer | Problem Solver)")

# --- Education ---
st.header("🎓 Education")
st.write("**Bachelor of Computer Science**, University Name (2021 - 2025)")
st.write("Relevant Coursework: Data Structures, Machine Learning, Software Engineering")

# --- Work Experience ---
st.header("💼 Work Experience")
st.subheader("Software Intern | Tech Company (Jun 2024 – Aug 2024)")
st.write("""
- Built a Streamlit dashboard to visualize customer analytics.  
- Automated daily reporting tasks using Python and Excel.  
- Improved system performance by 15%.  
""")

st.subheader("Freelance Web Developer (2023 – Present)")
st.write("""
- Developed responsive websites for small businesses.  
- Implemented booking systems and e-commerce features.  
""")

# --- Skills ---
st.header("🛠 Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("- Python")
    st.write("- SQL")
with col2:
    st.write("- Streamlit")
    st.write("- Git/GitHub")
with col3:
    st.write("- Problem Solving")
    st.write("- Communication")

# --- Projects ---
st.header("📂 Projects")
st.write("**Personal Portfolio Website** – Designed a personal website to showcase projects using Streamlit.")
st.write("**Data Analysis Project** – Analyzed sales data and built visual dashboards in Python.")
st.write("**Mobile App (Team Project)** – Created a professor appointment booking app with Flutter & Firebase.")

# --- Achievements ---
st.header("🏆 Achievements")
st.write("- Dean’s List (2022, 2023)")
st.write("- Winner, Hackathon 2024 – Built AI-powered study assistant")
st.write("- Certified in Google Data Analytics (2025)")
