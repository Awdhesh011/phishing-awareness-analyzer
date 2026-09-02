def calculate_url_risk(result):
    score = 0

    if not result["https"]:
        score += 10
    
    if result["has_ip"]:
        score += 25
    score += result["indicators"] * 10

    score = min(score, 100)

    if score <= 30:
            level = "Low"
    elif score <= 60:
            level = "Medium"
    else:
            level = "High"
    return {"score": score,
            "level": level
    }

def calculate_text_risk(result):
    score = result["indicators"] * 20

    score = min(score, 100)

    if score <= 30:
            level = "Low"
    elif score <= 60:
            level = "Medium"
    else:
            level = "High"
    return {"score": score,
            "level": level
    }