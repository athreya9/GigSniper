from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_leads():
    with open("data/leads.json") as f:
        leads = json.load(f)
    return jsonify(leads)

