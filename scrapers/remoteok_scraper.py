import requests
from scrapers.utils import extract_contacts

def scrape_remoteok():
    res = requests.get("https://remoteok.com/remote-jobs.json")
    jobs = res.json()

    leads = []
    # The first item is a legal notice, so we skip it.
    for job in jobs[1:11]:
        contacts = extract_contacts(job.get("description", ""))
        leads.append({
            "title": job["position"],
            "platform": "RemoteOK",
            "budget_type": "Unknown",
            "posted_days_ago": 0,
            "tags": job.get("tags", []),
            "link": job["url"],
            "contactEmail": contacts.get("email"),
            "contactPhone": contacts.get("phone"),
            "score": 0 # Placeholder score
        })
    return leads
