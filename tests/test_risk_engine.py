from src.risk_engine import calculate_url_risk,calculate_text_risk

def test_url_risk():
    result = {"https": False, 
              "has_ip": True, 
              "indicators":2
              }
    risk = calculate_url_risk(result)
    assert risk["score"] == 55
    assert risk["level"] == "Medium"

def test_text_risk():
    result = {"indicators":3}
    risk = calculate_text_risk(result)
    assert risk["score"] == 60
    assert risk["level"] =="Medium"
