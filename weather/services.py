
import requests


def get_metar(icao_code):

    url = "https://aviationweather.gov/api/data/metar"

    params = {
        "ids": icao_code,
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=15)

    response.raise_for_status()

    data = response.json()

    return data

def get_taf(icao_code):

    url="https://aviationweather.gov/api/data/taf"

    params={
        "ids": icao_code,
        "format":"json"
    }

    response=requests.get(url,params=params,timeout=15)

    if response.status_code==204:
        return []
    
    response.raise_for_status()

    return response.json()