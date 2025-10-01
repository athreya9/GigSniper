from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_leads():
    with open("data/leads.json") as f:
        leads = json.load(f)
    return jsonify(leads)

@app.route("/scrape", methods=["POST"])
def scrape_niche():
    data = request.get_json()
    niche = data.get("niche")

    if not niche:
        return jsonify({"error": "Niche keyword is required"}), 400

    # Here, you would implement the logic to map the niche to keywords
    # and trigger the scrapers. For now, we'll just return a success message.
    print(f"Received request to scrape for niche: {niche}")

    return jsonify({"message": f"Scraping for '{niche}' triggered successfully!"}), 200