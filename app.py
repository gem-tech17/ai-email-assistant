import streamlit as st
import time
from agent import process_email

st.set_page_config(page_title="AI Email Assistant", page_icon="📧")

st.title("📧 AI Email → Action Assistant")
st.write("Automate email understanding, task extraction, and reply generation using AI.")

email_input = st.text_area("Paste your email here:")

if st.button("Process"):
    if email_input:

        with st.spinner("Processing with AI..."):
            time.sleep(1.5)
            result = process_email(email_input)

        # ✅ Proper success check
        if isinstance(result, dict) and "summary" in result:

            st.subheader("📌 Summary")
            st.write(result["summary"])

            st.subheader("🎯 Intent")
            st.write(result["intent"])

            st.subheader("⚡ Priority")
            st.write(result["priority"])

            st.subheader("✅ Tasks")
            for task in result["tasks"]:
                st.write(f"- {task}")

            st.subheader("✉️ Suggested Reply")
            st.write(result["reply"])

        else:
            st.error("⚠️ AI output error")
            st.write(result)

    else:
        st.warning("⚠️ Please enter email text")