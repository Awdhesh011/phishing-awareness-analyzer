# 🛡️ Phishing Awareness Analyzer

A cybersecurity awareness tool that analyzes suspicious URLs and
messages for common phishing indicators and generates a risk score.

## 🚀 Features

- 🔗 URL phishing analysis
- 📧 Suspicious message analysis
- 🔍 Phishing indicator detection
- 📊 Risk score from 0–100
- 🟢 Low / 🟡 Medium / 🔴 High risk levels
- 📜 Analysis history
- 📥 Downloadable analysis report
- 🖥️ Streamlit web dashboard
- 🧪 Automated tests with pytest

## 🧠 How It Works

The analyzer checks different characteristics such as:

### URL Analysis

- HTTPS usage
- IP address instead of domain
- Suspicious URL keywords
- Other suspicious indicators

### Message Analysis

- Urgent or pressure-based language
- Suspicious keywords
- Requests for sensitive information

The detected indicators are converted into a risk score.

> This is an educational cybersecurity tool and does not guarantee
> that a URL or message is malicious.

## 🛠️ Technologies

- Python
- Streamlit
- Pytest
- Git & GitHub

## 📁 Project Structure

```text
phishing-awareness-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── url_analyzer.py
│   ├── text_analyzer.py
│   └── risk_engine.py
│
└── tests/
    ├── test_url_analyzer.py
    ├── test_text_analyzer.py
    └── test_risk_engine.py