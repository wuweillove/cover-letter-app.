import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Cover Letter Pro", page_icon="📄", layout="wide")

# --- SIDEBAR (THE MONEY PART) ---
with st.sidebar:
    st.header("💎 Premium Support")
    st.write("This tool is free to use. If it helps you get a job, buy me a coffee!")
    # REPLACE THE LINK BELOW WITH YOUR OWN BUYMEACOFFEE OR PAYPAL LINK
    st.markdown("[👉 **Click here to Donate $5**](buymeacoffee.com/coverletter") 
    st.markdown("---")
    st.write("Built for serious job seekers.")

# --- MAIN APP ---
st.title("📄 Professional Cover Letter Builder")
st.markdown("Generate a tailored, interview-ready cover letter in seconds.")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Step 1: Paste your Resume", height=300, placeholder="Paste your full resume text here...")
with col2:
    job = st.text_area("Step 2: Paste Job Description", height=300, placeholder="Paste the job description listing here...")

# --- CUSTOMIZATION ---
tone = st.selectbox("Choose Tone:", ["Professional & Formal", "Confident & Bold", "Casual & Modern"])

# --- GENERATION ---
if st.button("🚀 Generate My Letter", type="primary"):
    if not resume or not job:
        st.error("Please fill in both the Resume and Job Description boxes.")
    else:
        with st.spinner("Analyzing keywords and writing your letter..."):
            try:
                # Using the model that worked for you
                model = genai.GenerativeModel('gemini-flash-latest')
                
                prompt = f"""
                You are an expert career coach and professional copywriter. 
                Write a cover letter based on the provided resume and job description.
                
                TONE: {tone}
                
                INSTRUCTIONS:
                1. Analyze the Job Description for top 3 keywords.
                2. Match those keywords to skills in the Resume.
                3. Write a strong opening hook.
                4. Keep the letter under 350 words.
                5. Do NOT include placeholders like [Your Name] inside the body text if possible; make it flow naturally.
                
                RESUME DATA:
                {resume}
                
                JOB LISTING:
                {job}
                """
                
                response = model.generate_content(prompt)
                
                st.success("✅ Letter Generated Successfully!")
                st.subheader("Your Draft:")
                st.text_area("Copy and paste this into your application:", value=response.text, height=500)
                st.caption("Tip: Read through and make small edits to make it perfect.")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
