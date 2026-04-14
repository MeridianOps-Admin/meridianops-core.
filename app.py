import streamlit as st
import pandas as pd

# 1. PAGE SETUP
st.set_page_config(
    page_title="Meridian Ops | AI Audit",
    page_icon="🛡️",
    layout="wide"
)

# 2. THE "LUXURY TECH" STYLING (Forcing colors to override the Red)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Force Emerald Primary Color & Remove Red */
    .stButton>button {
        background-color: #10B981 !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: #1E293B !important;
    }

    /* Title & Headers */
    .main-header {
        font-size: 36px;
        font-weight: 600;
        color: #0F172A;
        margin-top: -40px;
    }
    .sub-header {
        font-size: 16px;
        color: #64748B;
        margin-bottom: 30px;
    }

    /* Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 15px;
        border-radius: 10px;
    }

    /* Remediation Cards */
    .card {
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #10B981;
        background-color: #F8FAFC;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (Text-based Logo to avoid broken images)
with st.sidebar:
    st.markdown("<h2 style='color: white; margin-bottom: 0;'>🛡️ Meridian</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size: 12px;'>AI COMPLIANCE ENGINE</p>", unsafe_allow_html=True)
    st.divider()
    st.button("Dashboard", use_container_width=True)
    st.button("Audit History", use_container_width=True)
    st.button("Compliance Vault", use_container_width=True)
    st.divider()
    st.caption("Status: **Operational**")
    st.caption("Core Engine: v2.4.0")

# 4. MAIN LAYOUT
st.markdown('<p class="main-header">Compliance Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Automated audit report for SOC 2 and regulatory alignment.</p>', unsafe_allow_html=True)

# Upload Area
uploaded_file = st.file_uploader("Upload your policy", type=["pdf", "txt"], label_visibility="collapsed")

if uploaded_file:
    st.divider()
    
    # Classification Badge
    st.success("**Document Identified:** Internal Data Retention Policy")

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Trust Score", "88/100", "+2")
    m2.metric("Risk Level", "Low")
    m3.metric("Critical Gaps", "0")
    m4.metric("Warnings", "3")

    # Findings
    st.markdown("### Detailed Findings")
    data = {
        "Requirement": ["Data Encryption", "Access Control", "Retention Period"],
        "Status": ["Compliant", "Partial", "Non-Compliant"],
        "Severity": ["-", "Medium", "High"]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    # Remediation
    st.markdown("### Required Actions")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""<div class="card"><strong>Update Retention Clause</strong><br><small>Section 4 must specify a 7-year storage limit.</small></div>""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""<div class="card"><strong>MFA Enforcement</strong><br><small>Update Section 2.1 to mandate hardware-based MFA.</small></div>""", unsafe_allow_html=True)

else:
    # Beautiful Empty State
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    empty_col1, empty_col2, empty_col3 = st.columns([1,2,1])
    with empty_col2:
        st.markdown("<div style='text-align: center; color: #94A3B8;'><h3>Ready to Audit</h3><p>Upload a PDF or TXT file to generate a real-time risk report.</p></div>", unsafe_allow_html=True)
