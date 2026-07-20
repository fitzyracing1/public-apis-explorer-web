#!/usr/bin/env python3
"""
Public APIs Explorer - Web Version
A simple web interface to explore popular public APIs.

Designed to run easily in Termux.
Run with: python app.py
Then open http://localhost:5000 in your browser (or Termux web access).
"""

from flask import Flask, render_template_string, request
from typing import List, Dict

app = Flask(__name__)

# Same bundled dataset as the CLI offline version
APIS = [
    {"name": "OpenWeatherMap", "description": "Weather data and forecasts", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Weather"},
    {"name": "WeatherAPI", "description": "Real-time weather information", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Weather"},
    {"name": "Google Maps", "description": "Maps, geocoding, directions", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Maps"},
    {"name": "GitHub API", "description": "Access GitHub repositories and user data", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Development"},
    {"name": "Spotify", "description": "Music streaming and metadata", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Music"},
    {"name": "YouTube Data", "description": "Search and manage YouTube videos", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Video"},
    {"name": "Twitter API v2", "description": "Access Twitter data and post tweets", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Social"},
    {"name": "Stripe", "description": "Payment processing", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Finance"},
    {"name": "CoinGecko", "description": "Cryptocurrency data and market info", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Finance"},
    {"name": "NASA APOD", "description": "Astronomy Picture of the Day", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Science"},
    {"name": "JokeAPI", "description": "Random jokes", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Entertainment"},
    {"name": "REST Countries", "description": "Country information", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Data"},
    {"name": "JSONPlaceholder", "description": "Fake REST API for testing", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Development"},
    {"name": "Dog CEO", "description": "Random dog images", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Animals"},
    {"name": "Cat Facts", "description": "Daily cat facts", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Animals"},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Public APIs Explorer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: system-ui, sans-serif; max-width: 900px; margin: 40px auto; padding: 20px; background: #f8f9fa; }
        h1 { color: #333; }
        .search-box { margin: 20px 0; }
        input[type="text"] { width: 70%; padding: 12px; font-size: 16px; border: 2px solid #ddd; border-radius: 8px; }
        button { padding: 12px 24px; font-size: 16px; background: #0066ff; color: white; border: none; border-radius: 8px; cursor: pointer; }
        .api-card { background: white; border-radius: 12px; padding: 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .api-name { font-size: 1.3em; font-weight: 600; color: #222; margin-bottom: 8px; }
        .meta { color: #666; font-size: 0.95em; }
        .tag { display: inline-block; background: #e0e7ff; color: #334; padding: 2px 10px; border-radius: 999px; font-size: 0.85em; margin-right: 8px; }
    </style>
</head>
<body>
    <h1>🌐 Public APIs Explorer</h1>
    <p>Search popular free APIs (offline version)</p>
    
    <form method="get" class="search-box">
        <input type="text" name="q" placeholder="Search APIs..." value="{{ query or '' }}">
        <button type="submit">Search</button>
    </form>

    {% if results %}
        <h3>Found {{ results|length }} results</h3>
        {% for api in results %}
        <div class="api-card">
            <div class="api-name">{{ api.name }}</div>
            <p>{{ api.description }}</p>
            <div class="meta">
                <span class="tag">{{ api.category }}</span>
                <span class="tag">Auth: {{ api.auth }}</span>
                <span class="tag">HTTPS: {{ api.https }}</span>
                <span class="tag">CORS: {{ api.cors }}</span>
            </div>
        </div>
        {% endfor %}
    {% elif query %}
        <p>No results found for "{{ query }}".</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    results = []
    
    if query:
        q = query.lower()
        results = [
            api for api in APIS 
            if q in api["name"].lower() or q in api["description"].lower()
        ]
    
    return render_template_string(HTML_TEMPLATE, results=results, query=query)

if __name__ == "__main__":
    print("Starting Public APIs Explorer Web UI...")
    print("Open http://localhost:5000 in your browser")
    app.run(host="0.0.0.0", port=5000, debug=True)
