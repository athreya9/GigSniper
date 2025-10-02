from playwright.sync_api import sync_playwright
from scrapers.utils import extract_contacts, compute_score

def scrape_bark():
    leads = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.bark.com/en/in/services/")
        cards = page.query_selector_all(".service-card")

        for card in cards[:10]:
            text = card.inner_text()
            contacts = extract_contacts(text)
            lead_data = {
                "title": card.query_selector("h3").inner_text(),
                "platform": "Bark",
                "budget_type": "Unknown",
                "posted_days_ago": 0,
                "tags": [],
                "link": page.url,
                "contactEmail": contacts.get("email"),
                "contactPhone": contacts.get("phone"),
            }
            lead_data["score"] = compute_score(lead_data)
            leads.append(lead_data)
        browser.close()
    return leads