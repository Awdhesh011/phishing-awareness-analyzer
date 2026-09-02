from src.url_analyzer import analyze_url

def test_https_url():
    result = analyze_url("https://www.example.com")
    assert result["https"] is True
    assert result["has_ip"] is False

    def test_ip_address_url():
        result = analyze_url("http://192.168.1.10/login")
        assert result["https"] is False
        assert result["has_ip"] is True
        assert result["indicator"] >= 2

    def test_suspicious_keywords():
        result = analyze_url("http://example.com/secure-login/verify-account")
        assert result["indicators"] >= 2
        assert result["suspicious"] is True
        