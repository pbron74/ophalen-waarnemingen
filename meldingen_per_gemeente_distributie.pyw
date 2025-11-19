import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import subprocess
import os
import sys

# ✅ Veilige import van scraper
try:
    from scrape_en_exporteer_distributie import scrape_en_exporteer, gemeente_dict
except Exception as e:
    print(f"❌ Fout bij importeren van scraper: {e}")
    gemeente_dict = {}

# 🧠 Functies voor extra scripts
def start_clustering():
    try:
        script_path = os.path.join(os.path.dirname(sys.argv[0]), "clustering_van_meldingen_distributie.pyw")
        subprocess.Popen([sys.executable, script_path])
    except Exception as e:
        status_var.set(f"❌ Fout bij starten clustering: {e}")

def start_vallenplan():
    try:
        script_path = os.path.join(os.path.dirname(sys.argv[0]), "vallenplan_met_keuzes.pyw")
        subprocess.Popen([sys.executable, script_path])
    except Exception as e:
        status_var.set(f"❌ Fout bij starten vallenplan: {e}")

# 🐝 Scrapingfunctie
def start_scraping():
    gemeente = gemeente_var.get()
    weken_str = weken_var.get()

    if not gemeente:
        status_var.set("❌ Kies een gemeente.")
        return

    gemeente_code = gemeente_dict.get(gemeente)
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
root = tk.Tk()
root.title("Aziatische hoornaar scraper")

gemeente_var = tk.StringVar()
weken_var = tk.StringVar(value="2")
status_var = tk.StringVar()

ttk.Label(root, text="Gemeente:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
gemeente_menu = ttk.Combobox(root, textvariable=gemeente_var, values=list(gemeente_dict.keys()), width=30)
gemeente_menu.grid(row=0, column=1, padx=10, pady=5)
gemeente_menu.set("Utrecht")  # standaardkeuze

ttk.Label(root, text="Aantal weken terug vanaf vandaag:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
ttk.Entry(root, textvariable=weken_var, width=5).grid(row=1, column=1, padx=10, pady=5, sticky="w")

ttk.Button(root, text="Start scraping", command=start_scraping).grid(row=2, column=0, columnspan=2, pady=10)
ttk.Label(root, textvariable=status_var, foreground="blue").grid(row=3, column=0, columnspan=2, pady=5)

ttk.Button(root, text="🧠 Start clustering", command=start_clustering).grid(row=4, column=0, columnspan=2, pady=5)
ttk.Button(root, text="🪤 Genereer vallenplan", command=start_vallenplan).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()


