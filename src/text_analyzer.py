SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "otp",
    "account",
    "suspended",
    "click",
    "login",
    "confirm",
    "bank",
]


def analyze_text(message):
    message_lower = message.lower()

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in message_lower:
            found_keywords.append(keyword)

    reasons = []
    indicators = 0

    # Suspicious keywords
    if found_keywords:
        reasons.append(
            "Suspicious keyword(s): " + ", ".join(found_keywords)
        )
        indicators += 1

    # Urgency detection
    urgent_words = [
        "urgent",
        "immediately",
        "right now",
        "within 24 hours",
    ]

    if any(word in message_lower for word in urgent_words):
        reasons.append(
            "Message uses urgent or pressure-based language"
        )
        indicators += 1

    # Credential request
    credential_words = [
        "password",
        "otp",
        "pin",
        "cvv",
    ]

    if any(word in message_lower for word in credential_words):
        reasons.append(
            "Message may be requesting sensitive information"
        )
        indicators += 1

    return {
        "suspicious": indicators >= 2,
        "indicators": indicators,
        "reasons": reasons,
        "keywords": found_keywords,
    }