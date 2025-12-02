from .scraper import scrape_en_exporteer
import json, os
from config import DATA_DIR

# Pad naar gemeenten.json
gemeenten_path = os.path.join(DATA_DIR, "gemeenten.json")

# Inlezen JSON-bestand
with open(gemeenten_path, encoding="utf-8") as f:
    gemeente_dict = json.load(f)
