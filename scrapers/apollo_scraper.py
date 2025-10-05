from playwright.sync_api import sync_playwright
from scrapers.utils import extract_contacts

def enrich_with_apollo(company_name, email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://app.apollo.io/#/login")

        page.fill("input[name='email']", email)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        page.wait_for_url("https://app.apollo.io/#/home")

        # Search for company
        page.goto(f"https://app.apollo.io/#/companies?search={company_name}")
        page.wait_for_selector(".CompanyCard")

        cards = page.query_selector_all(".CompanyCard")
        enriched = []

        for card in cards:
            name = card.query_selector(".CompanyCard__name").inner_text()
            website = card.query_selector(".CompanyCard__website").inner_text()
            description = card.query_selector(".CompanyCard__description").inner_text()
            contacts = extract_contacts(description + " " + website)
            enriched.append({
                "company": name,
                "website": website,
                "contactEmail": contacts.get("email"),
                "contactPhone": contacts.get("phone"),
            })

        browser.close()
        return enriched
