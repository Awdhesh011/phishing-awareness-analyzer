from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "password",
    "account",
    "secure",
    "update",
    "confirm",
]


def analyze_url(url):
    result = {
        "url": url,
        "https": False,
        "has_ip": False,
        "suspicious": False,
        "reasons": [],
        "indicators": 0
    }

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    # HTTPS check
    if parsed.scheme == "https":
        result["https"] = True
    else:
        result["reasons"].append("URL is not using HTTPS")
        result["indicators"] += 1

    # IP address check
    parts = hostname.split(".")

    if len(parts) == 4 and all(part.isdigit() for part in parts):
        result["has_ip"] = True
        result["reasons"].append(
            "URL uses an IP address instead of a domain name"
        )
        result["indicators"] += 1

    # @ symbol check
    if "@" in url:
        result["reasons"].append(
            "URL contains an @ symbol"
        )
        result["indicators"] += 1

    # URL length check
    if len(url) > 100:
        result["reasons"].append(
            "URL is unusually long"
        )
        result["indicators"] += 1

    # Subdomain check
    if hostname.count(".") >= 3:
        result["reasons"].append(
            "URL contains multiple subdomains"
        )
        result["indicators"] += 1

    # Suspicious keyword check
    url_lower = url.lower()

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in url_lower:
            found_keywords.append(keyword)

    if found_keywords:
        result["reasons"].append(
            "Suspicious keyword(s): " + ", ".join(found_keywords)
        )
        result["indicators"] += 1

    # Final suspicious decision
    if result["indicators"] >= 2:
        result["suspicious"] = True

    return result