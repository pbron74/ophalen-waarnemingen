import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import os
import sys
from config import GEMEENTEN_FILE, DATA_DIR   # ✅ GEMEENTEN_FILE voor lezen, DATA_DIR voor schrijven
from scrape_en_exporteer.scraper import scrape_en_exporteer
import json

# ✅ Gemeenten laden uit JSON (statisch resource-bestand)
try:
    with open(GEMEENTEN_FILE, "r", encoding="utf-8") as f:
        gemeente_dict = json.load(f)
    print(f"✅ {len(gemeente_dict)} gemeenten geladen uit JSON")
except Exception as e:
    print(f"❌ Fout bij laden van gemeenten.json: {e}")
    gemeente_dict = {}


# ✅ Directe imports van clustering en vallenplan
try:
    from clustering.clustering_logica import selecteer_bestand_en_straal
except Exception as e:
    print(f"❌ Fout bij importeren clustering_logica: {e}")
    selecteer_bestand_en_straal = None

try:
    from vallenplan.vallenplan_logica import start_gui as start_vallenplan_gui
except Exception as e:
    print(f"❌ Fout bij importeren vallenplan: {e}")
    start_vallenplan_gui = None

# 🔧 Helperfunctie: haal gekozen gemeente-ID op
def get_selected_gemeente_id(gemeente_var, gemeente_dict):
    gekozen = gemeente_var.get()
    return gemeente_dict.get(gekozen)

# 🧠 Start clustering direct
def start_clustering():
    if selecteer_bestand_en_straal is None:
        status_var.set("❌ Clustering module niet beschikbaar.")
        return
    try:
        selecteer_bestand_en_straal()
        status_var.set("✅ Clustering gestart")
    except Exception as e:
        status_var.set(f"❌ Fout bij clustering: {e}")

# 🧠 Start vallenplan direct
def start_vallenplan():
    if start_vallenplan_gui is None:
        status_var.set("❌ Vallenplan module niet beschikbaar.")
        return
    try:
        start_vallenplan_gui()
        status_var.set("✅ Vallenplan gestart")
    except Exception as e:
        status_var.set(f"❌ Fout bij vallenplan: {e}")

# 🐝 Scrapingfunctie
def start_scraping():
    gemeente = gemeente_var.get()
    weken_str = weken_var.get()

    if not gemeente:
        status_var.set("❌ Kies een gemeente.")
        return

    gemeente_code = get_selected_gemeente_id(gemeente_var, gemeente_dict)
    if not gemeente_code:
        status_var.set("❌ Gemeentecode niet gevonden.")
        return

    try:
        aantal_weken = int(weken_str)
        einddatum = datetime.today()
        startdatum = einddatum - timedelta(weeks=aantal_weken)
    except Exception as e:
        status_var.set(f"❌ Ongeldige invoer: {e}")
        return

    maandnaam = startdatum.strftime("%B")
    jaar = startdatum.year

    status_var.set(f"⏳ Ophalen voor {gemeente} ({aantal_weken} weken terug)...")
    root.update_idletasks()

    try:
        scrape_en_exporteer(startdatum, einddatum, maandnaam, jaar, gemeente, gemeente_code)
        status_var.set(f"✅ Klaar: bestanden opgeslagen voor {gemeente}")
    except Exception as e:
        status_var.set(f"❌ Fout tijdens scraping: {e}")

# 🖼️ GUI opbouw
def start_gui():
    global root, gemeente_var, weken_var, status_var

    root = tk.Tk()
    root.title("Aziatische hoornaar hoofdmenu")

    gemeente_var = tk.StringVar()
    weken_var = tk.StringVar(value="2")
    status_var = tk.StringVar()

    ttk.Label(root, text="Gemeente:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    gemeente_menu = ttk.Combobox(
        root,
        textvariable=gemeente_var,
        values=list(gemeente_dict.keys()),
        width=30,
        state="readonly"   # voorkomt vrije tekstinvoer
    )
    gemeente_menu.grid(row=0, column=1, padx=10, pady=5)

    # Standaardwaarde: Utrecht als die bestaat, anders eerste gemeente
    if "Utrecht" in gemeente_dict:
        gemeente_menu.set("Utrecht")
    else:
        eerste = next(iter(gemeente_dict.keys()), "")
        if eerste:
            gemeente_menu.set(eerste)

    ttk.Label(root, text="Aantal weken terug vanaf vandaag:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(root, textvariable=weken_var, width=5).grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ttk.Button(root, text="Start scraping", command=start_scraping).grid(row=2, column=0, columnspan=2, pady=10)
    ttk.Label(root, textvariable=status_var, foreground="blue").grid(row=3, column=0, columnspan=2, pady=5)

    ttk.Button(root, text="🧠 Start clustering", command=start_clustering).grid(row=4, column=0, columnspan=2, pady=5)
    ttk.Button(root, text="🪤 Genereer vallenplan", command=start_vallenplan).grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()

# 🚀 Entry point
if __name__ == "__main__":
    start_gui()