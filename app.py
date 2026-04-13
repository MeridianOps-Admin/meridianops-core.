import os
import streamlit as st
import fitz  # This is PyMuPDF for reading PDFs
from dotenv import load_dotenv
from openai import OpenAI

# 1. Boot up the vault silently
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Configure the Enterprise UI
st.set_page_config(page_title="MeridianOps Core", page_icon="🛡️", layout="centered")

st.title("🛡️ MeridianOps")
st.subheader("Automated SOC 2 Compliance Engine")
st.markdown("Upload internal policy documents (TXT or PDF) for instant regulatory auditing.")

# Security check before loading the app
if not api_key or api_key == "sk-your-actual-real-api-key-goes-here":
    st.error("SYSTEM HALT: Vault is empty. Secure your API key in the .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# 3. The Enterprise Upload Zone (Now supports PDF)
uploaded_file = st.file_uploader("Upload Company Policy", type=["txt", "pdf"])

# 4. The Execution Trigger
if st.button("Initialize SOC 2 Audit"):
    if uploaded_file is not None:
        
        document_text = ""
        
        # 5. The Extraction Engine
        with st.spinner("Extracting document data..."):
            try:
                if uploaded_file.name.endswith('.pdf'):
                    # Read PDF directly from memory
                    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                    for page_num in range(len(pdf_document)):
                        page = pdf_document.load_page(page_num)
                        document_text += page.get_text()
                else:
                    # Read standard TXT file
                    document_text = uploaded_file.getvalue().decode("utf-8")
            except Exception as e:
                st.error(f"SYSTEM ERROR: Failed to read document. Details: {e}")
                st.stop()
        
        # 6. The AI Audit Phase
        with st.spinner("Analyzing policy against SOC 2 regulatory frameworks..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4", 
                    messages=[
                        {"role": "system", "content": "You are a ruthless, highly accurate SOC 2 Compliance Auditor for an enterprise firm named MeridianOps. Analyze the provided company policy. Identify every security violation, explain why it fails SOC 2 compliance, and provide the mandatory correction. Output the response as a formal, professional audit report."},
                        {"role": "user", "content": f"AUDIT THIS POLICY:\n\n{document_text}"}
                    ]
                )
                
                # Output the result to the UI
                st.success("Audit Complete. Zero deviations missed.")
                st.markdown("### Official Audit Report")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"SYSTEM ERROR: Audit failed. Details: {e}")
    else:
        st.warning("USER ERROR: Please upload a policy document to proceed.")