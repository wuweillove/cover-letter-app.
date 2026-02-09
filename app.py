import streamlit as st
import google.generativeai as genai

# Configure the API key
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("🤖 Model Diagnoser")

if st.button("Check Available Models"):
    try:
        st.write("Asking Google...")
        # This asks for the list of models
        models = genai.list_models()
        
        found_any = False
        for m in models:
            # We only care about models that can 'generateContent' (write text)
            if 'generateContent' in m.supported_generation_methods:
                st.write(f"✅ Found: `{m.name}`")
                found_any = True
        
        if not found_any:
            st.error("No text-generation models found! Your API Key might be restricted.")
            
    except Exception as e:
        st.error(f"Error: {e}")

