import requests

ENERGY_MIX_URL = "https://www.ercot.com/api/1/services/read/dashboards/fuel-mix.json"


def load_energy_mix():
    """Downloads the energy mix JSON from ERCOT"""
    with requests.get(ENERGY_MIX_URL) as response:
        response.raise_for_status()
        return response.json()
