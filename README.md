De AHlauncher-macOS-dmg.zip
## 📦 Installatiehandleiding voor AHlauncher (macOS)

Volg deze stappen om AHlauncher op macOS te installeren:
1. **Download het bestand**
   - Klik op de downloadlink en haal `AHlauncher-macOS-dmg.zip` binnen.

2. **Pak het ZIP-bestand uit**
   - Dubbelklik op `AHlauncher-macOS-dmg.zip`.
   - Je krijgt nu het bestand `AHlauncher.dmg`.

3. **Open het DMG-bestand**
   - Dubbelklik op `AHlauncher.dmg`.
   - Er verschijnt een venster met het AHlauncher‑icoon en een snelkoppeling naar de **Applications** map.
   
+-----------------------------------------------------------+
|                                                           |
|   [ AHlauncher.app ]                                      |
|                                                           |
|                                                           |
|                                   [ Applications alias ]  |
|                                                           |
+-----------------------------------------------------------+

4. **Installeer de app**
   - Sleep het **AHlauncher‑icoon** naar de **Applications** map.
   - De app staat nu geïnstalleerd.

5. **Start AHlauncher**
   - Open de **Applications** map.
   - Dubbelklik op **AHlauncher** om de app te starten.
---
### ℹ️ Extra tips
- **Eerste keer openen:** macOS kan een waarschuwing geven (“app van onbekende ontwikkelaar”).  
  Ga dan naar **Systeemvoorkeuren → Beveiliging en privacy → Open toch** om de app te starten.
- **Verwijderen:** sleep AHlauncher gewoon uit de Applications map naar de prullenmand.
---
Met deze stappen heb je AHlauncher netjes geïnstalleerd op macOS 🎉.


Na opening van de app zie je dit hoofdmenu:
<img width="428" height="233" alt="afbeelding" src="https://github.com/user-attachments/assets/647f7d72-a57d-4dd3-aa76-0662b38d06b9" />


Functionaliteiten:
1) Ophalen van waarnemingen per gemeente voor de provincie Utrecht:
    De waarnemingen worden opgeslagen in een excel bestand in de Data map.
    Tevens wordt er een KML bestand aangemaakt die gewonload kan worden in MyMaps of GoogleEarth
    Elke nieuwe run voegt de nieuwe meldingen toe op basis van het aantal weken dat wordt aangegeven
    Verder worden de nestmeldingen gecontroleerd of deze doublures zijn en die worden in het bestnad aangegeven.

   Advies is om de data voor het gehele jaar op te halen. Voor de andere fucnties is het noodzakelijke om deze data te hebben.

2) Clustering van meldingen met en zonder nestmelding
    Er kan een straal worden gekozen tussen 300 – 700 m
    14 dagen na aanmelding nest worden nieuwe meldingen niet meer gekoppeld aan dat nest als ze binnen de straal vallen
    De output is 
        een interactieve kaart die je alle meldingen in cluster laat zien.
        interactief kunnen clusters met nest of zonder nest niet zichtbaar worden

   Het menu ziet er zo uit:
   <img width="514" height="323" alt="afbeelding" src="https://github.com/user-attachments/assets/982afbeb-ef3e-46c3-ab46-13de6aa21ddb" />

 4) Gebruiken voor het opstellen van een initieel selectieve vallen plan
        Huidige logica waar op de te plaatsen vallen worden aangegeven:
        Nesten na te kiezen datum na 1 september gemeld en Nesten voor een te keizen datum voor 1 juli waar binnen een straal van 200 m geen zomernesten zijn gevonden
        Vallen worden aangegeven met een straal van 70 m vanaf het nest en onderling
        Doublure nesten worden genegeerd.
        Er wordt een kaart gemaakt en geopend in je browser.

    Het menu ziet er zo uit:
    <img width="306" height="145" alt="afbeelding" src="https://github.com/user-attachments/assets/8131348c-cd00-4c27-95ce-81109e6dce3f" />



