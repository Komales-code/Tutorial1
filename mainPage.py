import streamlit as st


# Title
st.title("John Doe's Resume")

# Contact Information
st.header("📞 Contact Information")
st.write("📧 Email: john.doe@example.com")
st.write("📱 Phone: (123) 456-7890")
st.write("🔗 LinkedIn: [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)")

# Education
st.header("🎓 Education")
st.markdown("**B.Sc. in Computer Science**, University of Example, 2023")

# Work Experience
st.header("💼 Work Experience")
st.markdown("**Software Engineer Intern**, Example Corp (2023)")
st.write("- Developed and maintained internal tools using Python and Flask.")
st.write("- Collaborated with cross-functional teams to improve app performance.")

# Skills
st.header("🛠️ Skills")
skills = ["Python", "Streamlit", "SQL", "Git", "HTML/CSS"]
for skill in skills:
    st.write(f"- {skill}")

# Projects
st.header("📁 Projects")
st.markdown("**Portfolio Website** – A personal website built with HTML, CSS, and JavaScript to showcase my work.")
st.markdown("**Data Dashboard** – An interactive dashboard built using Streamlit and Pandas.")

# Optional: Add a Download Resume Button
with open("resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download My Resume", data=PDFbyte, file_name="John_Doe_Resume.pdf", mime='application/pdf')
