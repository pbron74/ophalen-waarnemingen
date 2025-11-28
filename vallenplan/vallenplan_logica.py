import pandas as pd
import folium
from tkinter import Tk, filedialog, messagebox, Label, Button, StringVar, OptionMenu, Entry
from geopy.distance import geodesic
from datetime import datetime
import math
import openpyxl
import re
import webbrowser
import os
from config import DATA_DIR

bestand_pad = None  # Globale variabele voor geselecteerd bestand

def parse_gps(gps_str):
    match = re.search(r'GPS\s*([\d.]+),\s*([\d.]+)', str(gps_str))
    if match:
        return float(match.group(1)), float(match.group(2))
    return None

def genereer_vallen(coord, afstand):
    vallen = []
    for hoek in range(0, 360, 45):
        dx = afstand * math.cos(math.radians(hoek))
        dy = afstand * math.sin(math.radians(hoek))
        lat_offset = dy / 111000
        lon_offset = dx / (111000 * math.cos(math.radians(coord[0])))
        vallen.append((coord[0] + lat_offset, coord[1] + lon_offset))
    return vallen

def lees_excel_met_links(filepath):
    df = pd.read_excel(filepath)
    df.columns = df.columns.str.strip()

    for col in df.columns:
        if str(col).strip().lower() == "doublure":
            df.rename(columns={col: "Doublure"}, inplace=True)

    wb = openpyxl.load_workbook(filepath, data_only=False)
    sheet = wb.active

    header = [cell.value for cell in next(sheet.iter_rows(min_row=1, max_row=1))]
    if 'Link' not in header:
        df['link_url'] = None
        return df

    link_col_index = header.index('Link') + 1
    urls = []
    for row in sheet.iter_rows(min_row=2):
        cell = row[link_col_index - 1]
        if cell.hyperlink:
            urls.append(cell.hyperlink.target)
        else:
            match = re.search(r'"(https?://[^"]+)"', str(cell.value))
            urls.append(match.group(1) if match else None)

    df['link_url'] = urls
    return df

def filter_nesten(df, datum_juli_str, datum_sep_str):
    df = df[df['Omschrijving'].str.contains("nest", case=False)].copy()
    df = df[~df['Doublure'].astype(str).str.strip().str.upper().isin(["WAAR", "TRUE", "1.0"])]
    df['Datum_parsed'] = pd.to_datetime(df['Datum_parsed'], errors='coerce')

    jaar_min = df['Datum_parsed'].dt.year.min()
    datum_juli = datetime.strptime(f"{datum_juli_str}-{jaar_min}", "%d-%m-%Y")
    datum_sep = datetime.strptime(f"{datum_sep_str}-{jaar_min}", "%d-%m-%Y")

    na_sep = df[df['Datum_parsed'] > datum_sep]
    voor_juli = df[df['Datum_parsed'] < datum_juli]
    na_juli = df[df['Datum_parsed'] >= datum_juli]

    unieke_nesten = []
    for _, rij in voor_juli.iterrows():
        coord_i = parse_gps(rij['GPS'])
        if coord_i is None:
            continue
        opvolgers = na_juli['GPS'].apply(lambda x: (
            parse_gps(x) is not None and geodesic(coord_i, parse_gps(x)).meters < 200
        ))
        if not opvolgers.any():
            unieke_nesten.append(rij)

    resultaat = pd.concat([na_sep, pd.DataFrame(unieke_nesten)])
    return resultaat

def maak_kaart(nesten_df, afstand, excel_pad, datum_juli_str, datum_sep_str):
    eerste_coord = parse_gps(nesten_df.iloc[0]['GPS'])
    kaart = folium.Map(location=eerste_coord, zoom_start=15)

    jaar_min = nesten_df['Datum_parsed'].dt.year.min()
    datum_juli = datetime.strptime(f"{datum_juli_str}-{jaar_min}", "%d-%m-%Y")
    datum_sep = datetime.strptime(f"{datum_sep_str}-{jaar_min}", "%d-%m-%Y")

    for _, rij in nesten_df.iterrows():
        nest_coord = parse_gps(rij['GPS'])
        if nest_coord is None:
            continue

        datum_val = rij['Datum_parsed']
        if pd.isna(datum_val):
            continue

        # kleur bepalen
        if datum_val < datum_juli:
            kleur = "green"   # Primaire nesten
        elif datum_val > datum_sep:
            kleur = "orange"  # Secundaire nesten
        else:
            continue  # tussen juli en september overslaan

        link = rij.get('link_url') or rij.get('Link')
        datum_str = datum_val.strftime("%d-%m-%Y")

        popup_html = (
            f"<b>Waarneming ID:</b> {rij['Waarneming ID']}<br>"
            f"<b>Datum:</b> {datum_str}<br>"
            f"{f'<a href={link} target=_blank>Bekijk melding</a>' if pd.notna(link) and str(link).startswith('https') else '<i>Geen link beschikbaar</i>'}"
        )

        folium.Marker(
            location=nest_coord,
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color=kleur, icon='info-sign')
        ).add_to(kaart)

        for val in genereer_vallen(nest_coord, afstand):
            folium.CircleMarker(location=val, radius=4, color='blue', fill=True, fill_opacity=0.6).add_to(kaart)

    # Legenda toevoegen
    legenda_html = f"""
    <div style="position: fixed; 
                top: 50px; left: 300px; width: 500px; height: 110px; 
                background-color: blank; border:2px solid grey; z-index:9999; font-size:14px;color: darkred;">
        <b>Legenda</b><br>
        <i style="color:green;">●</i> Primaire nesten en geen secundair binnen 200 m(voor {datum_juli_str})<br>
        <i style="color:orange;">●</i> Secundaire nesten (na {datum_sep_str})<br><br>
        <b>Afstand vallen tot nest en onderling=</b> {afstand} meter
    </div>
    """
    kaart.get_root().html.add_child(folium.Element(legenda_html))

    # Dynamische bestandsnaam
    bestandsnaam_input = os.path.basename(excel_pad)
    gemeente_naam = bestandsnaam_input.split('_')[0] if '_' in bestandsnaam_input else 'onbekend'
    gemeente_naam = gemeente_naam.replace(' ', '_')
    bestandsnaam_output = f"vallenplan_{gemeente_naam}.html"
    output_path = os.path.join(DATA_DIR, bestandsnaam_output)

    kaart.save(output_path)
    webbrowser.open(output_path)
    return output_path

def selecteer_bestand(root, afstand_var, datum_juli_entry, datum_sep_entry):
    global bestand_pad
    bestand_pad = filedialog.askopenfilename(initialdir=DATA_DIR, filetypes=[("Excel bestanden", "*.xlsx")])
    if not bestand_pad:
        messagebox.showwarning("Geen bestand", "Selecteer een Excel-bestand.")
        return

    try:
        afstand = int(afstand_var.get())
        df = lees_excel_met_links(bestand_pad)
        geselecteerde_nesten = filter_nesten(df, datum_juli_entry.get(), datum_sep_entry.get())

        if geselecteerde_nesten.empty:
            messagebox.showinfo("Geen nesten", "Er zijn geen geschikte nesten gevonden.")
        else:
            output_path = maak_kaart(geselecteerde_nesten, afstand, bestand_pad,
                                     datum_juli_entry.get(), datum_sep_entry.get())
            messagebox.showinfo("Kaart gereed", f"De kaart is opgeslagen in:\n{output_path}\n\nEn geopend in je browser.")

        root.destroy()
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden:\n{e}")
        root.destroy()

def start_gui():
    root = Tk()
    root.title("Nestkaart Generator")

    afstand_var = StringVar(root)
    afstand_var.set("70")
    afstand_opties = [str(x) for x in range(70, 151, 20)]

    Label(root, text="Afstand tot nest (m):").grid(row=0, column=0, sticky="w")
    OptionMenu(root, afstand_var, *afstand_opties).grid(row=0, column=1)

    Label(root, text="Datum vóór 1 juli (dd-mm):").grid(row=1, column=0, sticky="w")
    datum_juli_entry = Entry(root)
    datum_juli_entry.insert(0, "01-07")
    datum_juli_entry.grid(row=1, column=1)

    Label(root, text="Datum na 1 september (dd-mm):").grid(row=2, column=0, sticky="w")
    datum_sep_entry = Entry(root)
    datum_sep_entry.insert(0, "01-09")
    datum_sep_entry.grid(row=2, column=1)

    # Bestand selecteren triggert meteen uitvoeren + afsluiten
    Button(
        root,
        text="Selecteer Excel-bestand en genereer kaart",
        command=lambda: selecteer_bestand(root, afstand_var, datum_juli_entry, datum_sep_entry)
    ).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()


# Start de GUI als het script direct wordt uitgevoerd
if __name__ == "__main__":
    start_gui()