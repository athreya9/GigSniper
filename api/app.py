from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/leads", methods=["GET"])
def get_leads():
    with open("data/leads.json") as f:
        leads = json.load(f)
    return jsonify(leads)

# Vercel-compatible handler
def handler(environ, start_response):
    return app(environ, start_response)