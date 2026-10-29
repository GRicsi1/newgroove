"""
================================================================================
  NewGroove Tattoo — a weboldal szövegei és elérhetőségei
================================================================================
  Itt kell kicserélned az "egtext" helyőrzőket a saját adataidra.
  Mentés után elég újraindítani a szervert (python run.py).

================================================================================
"""

PLACEHOLDER = "egtext"

SITE = {
    "studioName": "NewGroove Tattoo",

    # Megjelenik a nyitóoldalon és a láblécben
    "address":   "1953 Öttevény, Leneskerti Utca valami",        # pl. Fő utca 12, Mosonmagyaróvár
    "phone":     "0620-----",        # pl. +36 30 123 4567
    "email":     "ide majd az email",        # a láblécben megjelenő kapcsolat e-mail cím
    "openHours": "ide majd a nyitvatartás",        # pl. Kedd–Szombat, 10:00–18:00

    # Közösségi média
    "instagramUrl":  "https://www.instagram.com/new_groove_tattoo/",    # teljes link, pl. https://instagram.com/felhasznalo
    "instagramName": "Instagram",    # a láblécben kiírt név, pl. @felhasznalo
    "facebookUrl":   "",    # teljes link

    # "A stúdió" szekció — tetszőleges számú művész (másolj be újabb blokkot, ha kell)
    "artists": [
        {"name": "Horváth Tamás", "role": "Tetováló", "bio": "Ide majd valami szép kis leírást kell küldj"},
    ],
}
