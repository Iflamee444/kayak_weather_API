import os
import pandas as pd
import requests as rq

API_KEY = "6f2adb4a3a5be330f97f688dc90405ac"
BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

villes = [
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier",
    "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble",
    "Dijon", "Angers", "Nîmes", "Villeurbanne", "Clermont-Ferrand", "Saint-Denis", "Le Mans",
    "Aix-en-Provence", "Brest", "Tours", "Amiens", "Limoges", "Annecy", "Perpignan",
    "Boulogne-Billancourt", "Metz", "Besançon", "Orléans", "Rouen"
]

csv_file = "cities_fr.csv"

if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=["city", "lat", "lon"])
    df.to_csv(csv_file, index=False, sep=';')

for ville in villes:
    params = {
        "q": f"{ville},FR",
        "limit": 1,
        "appid": API_KEY
    }
    response = rq.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            info = data[0]
            lat = info.get("lat")
            lon = info.get("lon")

            # Append to CSV
            new_row = pd.DataFrame([{"city": ville, "lat": lat, "lon": lon}])
            new_row.to_csv(csv_file, mode='a', header=False, index=False, sep=';')

            print(f"Added {ville}: lat={lat}, lon={lon}")
        else:
            print(f"No data for {ville}")
    else:
        print(f"Error {response.status_code} fetching {ville}")