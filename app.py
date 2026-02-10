import streamlit as st
import google.generativeai as genai
import datetime

# --- CONFIGURATION ---
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.set_page_config(page_title="Cover Letter Pro", page_icon="📄")

# --- DONATION LINK ---
donation_link = "https://www.buymeacoffee.com/coverletter"

# --- MAIN APP ---
st.title("📄 Professional Cover Letter Builder")
st.info(f"💡 **100% Free.** If this gets you a job, support me here: [**☕ Buy Me a Coffee**]({donation_link})")

col1, col2 = st.columns(2)
with col1:
    resume = st.text_area("Step 1: Paste Resume", height=300)
with col2:
    job = st.text_area("Step 2: Paste Job Description", height=300)

tone = st.selectbox("Choose Tone:", ["Professional", "Confident", "Casual"])

if st.button("🚀 Generate My Letter", type="primary"):
    if not resume or not job:
        st.error("Please fill in both boxes.")
    else:
        # --- THE TRACKER ---
        # This line prints a message to your private server logs
        print(f"[{datetime.datetime.now()}] 💰 SOMEONE JUST GENERATED A LETTER!")
        
        with st.spinner("Writing..."):
            try:
                model = genai.GenerativeModel('gemini-flash-latest')
                prompt = f"Write a cover letter. Tone: {tone}. Resume: {resume}. Job: {job}"
                response = model.generate_content(prompt)
                
                st.success("✅ Done!")
                st.text_area("Result:", value=response.text, height=400)
                st.markdown(f"[**👉 Donate $5**]({donation_link})")
                
            except Exception as e:
                st.error(f"Error: {e}")
