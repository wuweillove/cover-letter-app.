import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Cover Letter Pro", page_icon="📄")

# --- MAIN TITLE & DONATION (TOP) ---
st.title("📄 Cover Letter Pro")
st.write("Generate a tailored, interview-ready cover letter in seconds.")

# This is the new "Money" section - distinct and visible
st.info("💡 **This tool is 100% free.** If it helps you get a job, you can support me here: [**☕ Buy Me a Coffee ($5)**](https://www.buymeacoffee.com)")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Step 1: Paste Resume", height=300, placeholder="Paste your resume text here...")
with col2:
    job = st.text_area("Step 2: Paste Job Description", height=300, placeholder="Paste the job listing here...")

# --- CUSTOMIZATION ---
tone = st.selectbox("Choose Tone:", ["Professional & Formal", "Confident & Bold", "Casual & Modern"])

# --- GENERATION ---
if st.button("🚀 Generate My Letter", type="primary"):
    if not resume or not job:
        st.error("Please fill in both the Resume and Job Description boxes.")
    else:
        with st.spinner("Writing your letter..."):
            try:
                # Using the generic flash model
                model = genai.GenerativeModel('gemini-flash-latest')
                
                prompt = f"""
                You are an expert career coach. Write a cover letter based on this resume and job.
                TONE: {tone}
                RESUME: {resume}
                JOB: {job}
                """
                
                response = model.generate_content(prompt)
                
                st.success("✅ Done! Copy your letter below.")
                st.text_area("Result:", value=response.text, height=400)
                
                # --- SECOND DONATION PROMPT (BOTTOM) ---
                st.markdown("---")
                st.write("Did this save you time? 👇")
                st.markdown("[**👉 Click here to Donate $5**](buymeacoffee.com/coverletter)")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
