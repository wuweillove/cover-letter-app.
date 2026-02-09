import streamlit as st
import google.generativeai as genai

# 1. CONFIGURATION
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. APP LAYOUT
st.set_page_config(page_title="QuickCover AI", page_icon="📝")
st.title("💸 QuickCover AI")
st.markdown("### Generate a professional cover letter in seconds.")

col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Paste Resume Here:", height=300)
with col2:
    job = st.text_area("Paste Job Description Here:", height=300)

# 3. GENERATION LOGIC
if st.button("🚀 Generate Letter"):
    if not resume or not job:
        st.error("Please fill in both boxes!")
    else:
        with st.spinner("Writing your letter..."):
            try:
                # We are using "gemini-flash-latest" to find the best working model for you
                model = genai.GenerativeModel('gemini-flash-latest')
                
                prompt = f"""
                You are an expert career coach. Write a professional cover letter 
                based on this resume and job description. 
                
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
st.caption("Powered by Google Gemini")
