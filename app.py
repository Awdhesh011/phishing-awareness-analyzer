import streamlit as st
from datetime import datetime

from src.url_analyzer import analyze_url
from src.text_analyzer import analyze_text
from src.risk_engine import calculate_url_risk, calculate_text_risk


st.set_page_config(
    page_title="Phishing Awareness Analyzer",
    page_icon="🛡️",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []

#-----------------------------
# Helper Functions
#-----------------------------
def show_risk(score, level):
    if level == "Low":
       st.success (f"🟢 {level} Risk - {score}/100")
    elif level == "Medium":
        st.warning(f"🟡 {level} Risk - {score}/100")
    else:
        st.error(f"🔴 {level} Risk - {score}/100")

#-----------------------------
# Header
#-----------------------------

st.title("🛡️ Phishing Awareness Analyzer")
st.write(
    "Analyze suspicious URLs and messages for common phishing indicators."
)

st.warning(
    "⚠️ This tool provides a risk estimate based on detected indicators. "
    "It does not guarantee that a URL or message is malicious."
)


# -----------------------------
# URL ANALYZER
# -----------------------------

st.header("🔗 URL Analyzer")

url = st.text_input(
    "https://example.com/suspicious-url",
    placeholder="https://example.com/suspicious-url"
)

if st.button("Analyze URL"):

    if not url:
        st.error("Please enter a URL.")

    else:
        result = analyze_url(url)
        risk = calculate_url_risk(result)
        st.session_state.history.append({"time": datetime.now().strftime("%H:%M:%S"), "type": "URL", 
        "input": url, "score": risk["score"], "level": risk["level"]})
        st.subheader("Analysis Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", f"{risk['score']}/100")

        with col2:
            st.metric("Risk Level", risk["level"])

        with col3:
            st.metric(
                "Indicators",
                result["indicators"]
            )

        st.write("### 🔍 Detected Indicators")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.write("⚠️", reason)
        else:
            st.success("No obvious suspicious indicators detected.")


# -----------------------------
# MESSAGE ANALYZER
# -----------------------------

st.header("📧 Message Analyzer")

message = st.text_area(
    "Enter a suspicious message:",
    height=180,
    placeholder="paste message here..."
)

if st.button("Analyze Message"):

    if not message:
        st.error("Please enter a message.")

    else:
        result = analyze_text(message)
        risk = calculate_text_risk(result)
        st.session_state.history.append({"time": datetime.now().strftime("%H:%M:%S"), "type": "Message",
        "input": message, "score": risk["score"], "level": risk["level"]})

        st.subheader("Message Analysis Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", f"{risk['score']}/100")

        with col2:
            st.metric("Risk Level", risk["level"])

        with col3:
            st.metric(
                "Indicators",
                result["indicators"]
            )

        st.write("### 🔍 Detected Indicators")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.write("⚠️", reason)
        else:
            st.success("No obvious suspicious indicators detected.")

# -----------------------------
# Safety Advice
# -----------------------------
st.divider()
st.header("🛡️ Phishing Safety Tips ")
st.write(""" 
-Never share your password, otp, or personal information with anyone.
-Always verify the sender's email address or phone number.
-Check domain names carefully for misspellings or unusual characters.
-Avoid clicking on links in unsolicited messages; instead, type the URL directly into your browser.
""")
st.divider()
st.header("📜 Analysis History")
if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write(f"**{item['time']} | {item['type']} | "f"{item['level']} risk | Score: {item['score']}/100**")
        st.caption (item["input"])
else:
    st.info("No analysis history yet. Perform an analysis to see results here.")
    st.divider()
    st.header("📩 Download Report")
    if st.session_state.history:
        report_lines = []
        report_lines.append("Phishing Awareness Analyzer Report")
        report_lines.append("=" * 40)
        report_lines.append("")
        for item in st.session_state.history:
            report_lines.append(f"Time: {item['time']}")
            report_lines.append(f"Type: {item['type']}")
            report_lines.append(f"Risk Level: {item['level']}")
            report_lines.append(f"Score: {item['score']}/100")
            report_lines.append("Input:")
            report_lines.append(item["input"])
            report_lines.append("-" * 40)
            report = "\n".join(report_lines)
            st.download_button(label="📄 Download Report", data=report, file_name="phishing_analysis_report.txt",
                mime="text/plain")
        else:
            st.info("No analysis history yet. Perform an analysis to generate a report.")