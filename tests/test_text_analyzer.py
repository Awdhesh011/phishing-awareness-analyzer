from src.text_analyzer import analyze_text


def test_phishing_message():
    message = """
    URGENT! Your account has been suspended.
    Verify your account immediately.
    Enter your password and OTP.
    """

    result = analyze_text(message)

    assert result["suspicious"] is True
    assert result["indicators"] >= 2


def test_normal_message():
    message = "Hello, have a nice day."

    result = analyze_text(message)

    assert result["suspicious"] is False