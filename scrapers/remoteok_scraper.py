import requests
from bs4 import BeautifulSoup
from scrapers.utils import extract_contacts

def scrape_remoteok():
    res = requests.get("https://remoteok.com/")
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = soup.select("tr.job")

    leads = []
    for job in jobs[:10]:
        title = job.select_one("h2").text.strip()
        link = "https://remoteok.com" + job["data-href"]
        contacts = extract_contacts(job.text)
        leads.append({
            "title": title,
            "platform": "RemoteOK",
            "budget_type": "Unknown",
            "posted_days_ago": 0,
            "tags": [],
            "link": link,
            **contacts
        })
    return leads