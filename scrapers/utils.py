import re

def extract_contacts(text):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phones = re.findall(r"\+?\d[\d -]{8,}\d", text)
    websites = re.findall(r"https?://[^\s]+", text)
    return {
        "email": emails[0] if emails else None,
        "phone": phones[0] if phones else None,
        "website": websites[0] if websites else None
    }

def compute_score(lead):
    score = 0
    if lead.get("contactEmail"):
        score += 40
    if lead.get("contactPhone"):
        score += 40
    if lead.get("tags") and len(lead["tags"]) > 0:
        score += 20
    return score
