import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# This gets your secret key from Streamlit
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Cover Letter Pro", page_icon="📄")

# --- YOUR DONATION LINK ---
# I added your specific link here
donation_link = "https://www.buymeacoffee.com/coverletter"

# --- MAIN TITLE ---
st.title("📄 Professional Cover Letter Builder")
st.write("Generate a tailored, interview-ready cover letter in seconds.")

# --- DONATION BOX (TOP) ---
# This puts a blue box at the top with your link
st.info(f"💡 **This tool is 100% free.** If it helps you get a job, you can support me here: [**☕ Buy Me a Coffee**]({donation_link})")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Step 1: Paste Resume", height=300, placeholder="Paste your resume text here...")
with col2:
    job = st.text_area("Step 2: Paste Job Description", height=300, placeholder="Paste the job listing here...")

# --- CUSTOMIZATION ---
tone = st.selectbox("Choose Tone:", ["Professional & Formal", "Confident & Bold", "Casual & Modern"])

# --- GENERATION BUTTON ---
if st.button("🚀 Generate My Letter", type="primary"):
    if not resume or not job:
        st.error("Please fill in both the Resume and Job Description boxes.")
    else:
        with st.spinner("Writing your letter..."):
            try:
                # Using the latest Flash model (fast & free)
                model = genai.GenerativeModel('gemini-flash-latest')
                
                prompt = f"""
                You are an expert career coach. Write a cover letter based on this resume and job.
                
                TONE: {tone}
                
                RESUME:
                {resume}
                
                JOB DESCRIPTION:
                {job}
                """
                
                response = model.generate_content(prompt)
                
                # --- SUCCESS & RESULT ---
                st.success("✅ Done! Copy your letter below.")
                st.text_area("Result:", value=response.text, height=400)
                
                # --- DONATION REMINDER (BOTTOM) ---
                st.markdown("---")
                st.write("Did this save you time? 👇")
                st.markdown(f"[**👉 Click here to Donate $5**]({donation_link})")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
