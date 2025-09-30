import requests
from scrapers.utils import extract_contacts

def scrape_reddit():
    url = "https://www.reddit.com/r/forhire/new.json?limit=10"
    headers = {"User-Agent": "GigSniperBot"}
    res = requests.get(url, headers=headers)
    print(res.status_code)
    print(res.text)
    posts = res.json()["data"]["children"]

    leads = []
    for post in posts:
        data = post["data"]
        contacts = extract_contacts(data.get("selftext", ""))
        leads.append({
            "title": data["title"],
            "platform": "Reddit",
            "budget_type": "Unknown",
            "posted_days_ago": 0,
            "tags": [],
            "link": f"https://reddit.com{data['permalink']}",
            **contacts
        })
    return leads