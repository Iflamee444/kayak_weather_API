Author :
  RAVELOSON Marius Mamiarisoa

# KAYAK Last Minutes

## Description

Ce projet permet de trouver des hôtels de dernières minutes dans les villes avec un météo agréable pendant les 5 prochains jours dans la France

### RETOUR
   * Carte météo des villes.
   * Carte des hôtels avec note et coordonnées.

Le projet utilise des fichiers CSV pour stocker les données intermédiaires :

* `cities_fr.csv` → coordonnées des villes.
* `top_cities.csv` → météo des villes.
* `hotels.csv` → hôtels et leurs notes.

---

## Structure du projet

```
project/
│
├─ init.py               # Script principal, lance tous les modules dans l'ordre
├─ settings.py           # Contient API_KEY, URL et listes de villes
├─ weather_city.py       # et_city_weather() : récupère météo
├─ map.py                # get_map_weather() : carte météo
├─ hotels_list.py        # get_hotel_per_city() : scrape Booking.com
├─ hotel_map.py          # hotel_map_maker() : carte hôtels
├─ cities_fr.csv         # Coordonnées des villes (généré automatiquement)
├─ top_cities.csv        # Météo des villes (généré automatiquement)
├─ hotels.csv            # Liste des hôtels (généré automatiquement)
├─ README.md
├─ test.ipipnb           # pour tester si tout marche bien
└─ requirements.txt
```

---

## Installation

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

3. Configurer `settings.py` avec votre clé OpenWeather API (`API_KEY`) et la liste de villes.

---

## Utilisation

Lancer **init.py** pour exécuter tout le workflow :

```bash
python init.py
```

## Requirements

Voir `requirements.txt`.
