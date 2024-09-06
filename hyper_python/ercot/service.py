from . import loader
from .model.fuel_mix import FuelMix


def get_energy_mix() -> FuelMix:
    """ Loads fuel mix json and returns as FuelMix object."""
    json = loader.load_energy_mix()
    return FuelMix(json)