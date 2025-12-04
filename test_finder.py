# test_finder.py
from config import GEMEENTEN_FILE
import os, json

print("CWD =", os.getcwd())
print("GEMEENTEN_FILE =", GEMEENTEN_FILE)

try:
    with open(GEMEENTEN_FILE, "r", encoding="utf-8") as f:
        gemeenten = json.load(f)
    print(f"✅ {len(gemeenten)} gemeenten geladen uit JSON")
except Exception as e:
    print(f"❌ Kon gemeenten.json niet laden: {e}")
