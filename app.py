import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Meridian | AI Risk & Compliance",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. LUXURY TECH STYLING (CSS)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Import Premium Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B; /* Deep Slate */
    }

    /* Main Background */
    .stApp {
        background-color: #FFFFFF;
    }

    /* Custom Title & Subtitle */
    .main-title {
        font-size: 42px;
        font-weight: 600;
        letter-spacing: -1.5px;
        color: #0F172A;
        margin-bottom: 8px;
    }
    .sub-title {
        font-size: 18px;
        font-weight: 300;
        color: #64748B;
        margin-bottom: 40px;
    }

    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background-color: #F8FAFC;
        border: 1px solid #F1F5F9;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    div[data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 600;
        color: #0F172A;
    }

    /* Classification Badge */
    .badge {
        padding: 8px 16px;
        border-radius: 100px;
        font-weight: 500;
        font-size: 14px;
        display: inline-block;
        margin-bottom: 20px;
    }
    .badge-policy { background-color: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; }

    /* Remediation Cards */
    .remediation-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #10B981; /* Emerald Tech Accent */
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 16px;
        transition: transform 0.2s ease;
    }
    .remediation-card:hover {
        border-color: #CBD5E1;
        transform: translateY(-2px);
    }
    
    /* Clean Table Styling */
    .stDataFrame {
        border: none;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=MERIDIAN", width=150) # Replace with your logo
    st.markdown("---")
    st.markdown("### Navigation")
    st.button("Dashboard", use_container_width=True, type="primary")
    st.button("Audit History", use_container_width=True)
    st.button("Settings", use_container_width=True)
    st.markdown("---")
    st.caption("System Status: **Operational**")
    st.caption("Compliance Engine: **v2.4.0**")

# ---------------------------------------------------------
# 4. TOP AREA: TITLE & UPLOAD
# ---------------------------------------------------------
st.markdown('<p class="main-title">Meridian Audit</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Verify document compliance against global regulatory standards.</p>', unsafe_allow_html=True)

# Centering the upload box slightly
upload_col1, upload_col2 = st.columns([2, 1])
with upload_col1:
    uploaded_file = st.file_uploader("Drop document here", type=["pdf", "docx", "txt"], label_visibility="collapsed")

# ---------------------------------------------------------
# 5. AUDIT REPORT FLOW
# ---------------------------------------------------------
if uploaded_file:
    st.markdown("---")
    
    # A. Document Classification
    st.markdown('<div class="badge badge-policy">Analysis Complete: **Internal Privacy Policy**</div>', unsafe_allow_html=True)

    # B. Overall Score & Risk + C. Severity Counts
    m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)
    with m_col1:
        st.metric("Trust Score", "84/100", delta="High")
    with m_col2:
        st.metric("Risk Level", "Low-Mid")
    with m_col3:
        st.metric("Critical Gaps", "0")
    with m_col4:
        st.metric("High Priority", "3")
    with m_col5:
        st.metric("Advisory", "7")

    st.markdown("<br>", unsafe_allow_html=True)

    # D. Executive Summary
    with st.container():
        st.markdown("### Executive Summary")
        st.info("""
        The uploaded document demonstrates strong alignment with GDPR and CCPA frameworks. 
        The primary areas of concern involve **Third-Party Data Processing** and **Automated Decision-Making** disclosures which lack specific technical citations. Remediation is recommended for Section 8.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # E. Findings Table
    st.markdown("### Detailed Findings")
    findings_data = {
        "ID": ["FIN-001", "FIN-002", "FIN-003"],
        "Requirement": ["Art. 30 GDPR", "CCPA §1798.100", "Transparency"],
        "Observation": ["Data controller contact info is missing.", "Right to delete not clearly defined.", "Sub-processor list is outdated."],
        "Status": ["High Priority", "Medium", "High Priority"]
    }
    df = pd.DataFrame(findings_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # F. Remediation Cards
    st.markdown("### Strategic Remediation")
    
    remediation_items = [
        {
            "title": "Update Contact Disclosure",
            "body": "Insert the specific legal name and registered address of the Data Protection Officer (DPO) in the introductory clause."
        },
        {
            "title": "Define Deletion Protocols",
            "body": "Explicitly state the 30-day window for processing user data deletion requests to satisfy CCPA requirements."
        },
        {
            "title": "Sub-Processor API Sync",
            "body": "Link the document to the live Sub-Processor registry to ensure real-time accuracy of third-party disclosures."
        }
    ]

    for item in remediation_items:
        st.markdown(f"""
            <div class="remediation-card">
                <div style="font-weight:600; font-size:18px; color:#0F172A; margin-bottom:8px;">{item['title']}</div>
                <div style="font-size:15px; color:#475569; line-height:1.5;">{item['body']}</div>
            </div>
        """, unsafe_allow_html=True)

else:
    # Empty State
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.center_column = st.columns([1, 2, 1])
    with st.center_column[1]:
        st.image("https://via.placeholder.com/400x300?text=Waiting+for+Document...", use_container_width=True)
        st.caption("Upload a policy or procedure to generate your first audit report.")
