import json
from datetime import datetime
from scrapers.reddit_scraper import scrape_reddit
# from scrapers.bark_scraper import scrape_bark
from scrapers.remoteok_scraper import scrape_remoteok
# from scrapers.outbounders_scraper import scrape_outbounders

def refresh_leads():
    all_leads = []
    reddit_leads = scrape_reddit()
    print(f"Refresh: Scraped {len(reddit_leads)} leads from Reddit.")
    all_leads += reddit_leads

    # bark_leads = scrape_bark()
    # print(f"Refresh: Scraped {len(bark_leads)} leads from Bark.")
    # all_leads += bark_leads

    remoteok_leads = scrape_remoteok()
    print(f"Refresh: Scraped {len(remoteok_leads)} leads from RemoteOK.")
    all_leads += remoteok_leads

    # outbounders_leads = scrape_outbounders()
    # print(f"Refresh: Scraped {len(outbounders_leads)} leads from Outbounders.")
    # all_leads += outbounders_leads

    payload = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "leads": all_leads
    }

    with open("data/leads.json", "w") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    refresh_leads()