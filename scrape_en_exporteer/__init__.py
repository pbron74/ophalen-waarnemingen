from .scraper import scrape_en_exporteer
import json, os
from config import GEMEENTEN_FILE, DATA_DIR

# Pad naar gemeenten.json (statisch resource-bestand)
gemeenten_path = GEMEENTEN_FILE

# Inlezen JSON-bestand
with open(gemeenten_path, encoding="utf-8") as f:
    gemeente_dict = json.load(f)

