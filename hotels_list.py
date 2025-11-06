import pandas as pd
import requests as rq
from scrapy import Selector
import time
import os

from settings import BASE_URL_BK, HEADERS, TIMEOUT

OUTPUT_FILE = "output/hotels.csv"

def get_hotel_per_city():
    df = pd.read_csv("output/top_cities.csv", sep=';')
    villes = df["city"].astype(str).unique()

    if not os.path.exists(OUTPUT_FILE):
        df = pd.DataFrame(columns=["ville", "name", "rating"])
        df.to_csv(OUTPUT_FILE, index=False, sep=';')

    for ville in villes:
        url = f"{BASE_URL_BK}searchresults.fr.html?ss={ville}&dest_type=city&order=popularity"
        response = rq.get(url, headers=HEADERS, timeout=TIMEOUT)
        selector = Selector(text=response.text)

        all_hotels = []

        fiche = selector.css("div[data-testid='property-card']")
        if not fiche:
            fiche = selector.css(".sr_property_block")

        for i, card in enumerate(fiche[:5], start=1):
            name = card.css("[data-testid='title']::text, .sr-hotel__name::text").get()
            rating = card.css("[data-testid='review-score'] ::text, .bui-review-score__badge::text").get()
            if rating:
                rating = rating.strip().replace("Avec une note de ", "")

            all_hotels.append({
                "ville": ville,
                "name": name.strip() if name else None,
                "rating": rating.strip() if rating else None,
            })

        time.sleep(3.0)

        df_out = pd.DataFrame(all_hotels)
        df_out.to_csv(OUTPUT_FILE, mode='a', header=False, index=False, sep=';')
