"""
PRIVACY RESET UTILITY
=====================
This script clears all cached profile data and session state.
Run this to remove any personal information from the app's session.
"""

import streamlit as st

st.set_page_config(page_title="Reset Profile Data", page_icon="🔒")

st.title("🔒 Privacy Data Reset")
st.warning("⚠️ This will clear ALL profile data and session information")

if st.button("🗑️ CLEAR ALL DATA", type="primary"):
    # Clear all session state
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    st.success("✅ All session data cleared!")
    st.balloons()
    st.info("👉 Please close and reopen the app, or clear your browser cache/cookies")
    
st.divider()

st.markdown("""
### What gets cleared:
- User profile information
- Generated cover letters
- Letter history and versions
- All preferences and settings
- Session cache

### Additional steps:
1. Clear your browser cookies for this site
2. Clear browser cache
3. Restart the Streamlit app if running locally
4. For deployed apps, the Streamlit Cloud cache may need manual clearing

### Prevention:
- Never commit actual profile data to version control
- Use .gitignore for local data files
- Keep example data generic
""")
