import streamlit as st
import google.generativeai as genai

# This looks for your secret key in the system settings
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("💸 QuickCover AI")
st.write("Paste your info below to generate a professional cover letter instantly.")

# The Inputs
col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Paste Resume Here", height=300)
with col2:
    job = st.text_area("Paste Job Description Here", height=300)

# The Button
if st.button("Generate Letter"):
    if not resume or not job:
        st.error("Please fill in both boxes!")
    else:
        with st.spinner("Thinking..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')

                prompt = f"Write a professional cover letter for this resume: {resume} \n for this job: {job}"
                response = model.generate_content(prompt)
                st.success("Done! Copy below:")
                st.text_area("Result", response.text, height=400)
            except Exception as e:
                st.error(f"Error: {e}")
