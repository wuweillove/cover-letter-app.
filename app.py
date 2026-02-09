import streamlit as st
import google.generativeai as genai

# 1. SETUP: Get the API key from the "Secrets" we saved earlier
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. THE APP DESIGN
st.set_page_config(page_title="QuickCover AI", page_icon="📝")
st.title("💸 QuickCover AI")
st.markdown("### Generate a professional cover letter in seconds.")

# 3. THE INPUTS
col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Paste Resume Here:", height=300)
with col2:
    job = st.text_area("Paste Job Description Here:", height=300)

# 4. THE MAGIC BUTTON
if st.button("🚀 Generate Letter"):
    if not resume or not job:
        st.error("Please fill in both boxes!")
    else:
        with st.spinner("Writing your letter using Gemini 2.0..."):
            try:
                # WE USE THE EXACT MODEL NAME FOUND IN YOUR LIST
                # Use the "latest" alias which usually has the best free tier availability
model = genai.GenerativeModel('gemini-flash-latest')
                
                prompt = f"""
                You are an expert career coach. Write a professional, persuasive cover letter 
                based on this resume and job description. 
                
                RULES:
                1. Keep it concise (under 300 words).
                2. Use a confident, human tone (not robotic).
                3. Highlight specific skills from the resume that match the job.
                
                RESUME:
                {resume}
                
                JOB DESCRIPTION:
                {job}
                """
                
                response = model.generate_content(prompt)
                
                st.success("Your Cover Letter is ready!")
                st.text_area("Copy your letter:", value=response.text, height=400)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Powered by Gemini 2.0 Flash")
