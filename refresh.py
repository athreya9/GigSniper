import json
from datetime import datetime
from scrapers.reddit_scraper import scrape_reddit
from scrapers.bark_scraper import scrape_bark
from scrapers.remoteok_scraper import scrape_remoteok

def refresh_leads():
    all_leads = []
    all_leads += scrape_reddit()
    all_leads += scrape_bark()
    all_leads += scrape_remoteok()

    payload = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "leads": all_leads
    }

    with open("data/leads.json", "w") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    refresh_leads()