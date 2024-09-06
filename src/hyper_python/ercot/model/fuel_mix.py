from ...helper import datetime_helper
from ... import DATETIME_FORMAT

from enum import Enum
from datetime import datetime

class RenewableFuel(Enum):
    WIND = "Wind"
    HYDRO = "Hydro"
    SOLAR = "Solar"
    NUCLEAR = "Nuclear"
    POWER_STORAGE = "Power Storage"

class DirtyFuel(Enum):
    COAL = "Coal and Lignite"
    OTHER = "Other"
    NATURAL_GAS = "Natural Gas"

class FuelMixDetails:
    def __init__(self, fuel_mix: dict[str, float], date: datetime):
        self.fuel_mix = fuel_mix
        self.date = date

    def get_total_generation(self) -> float:
        return sum(self.fuel_mix.values())

    def get_renewable_generation(self) -> float:
        return (self.fuel_mix[RenewableFuel.WIND.value] +
                self.fuel_mix[RenewableFuel.HYDRO.value] +
                self.fuel_mix[RenewableFuel.SOLAR.value] +
                self.fuel_mix[RenewableFuel.NUCLEAR.value] +
                self.fuel_mix[RenewableFuel.POWER_STORAGE.value])

    def get_renewable_percentage(self) -> float:
        return self.get_renewable_generation() / self.get_total_generation() * 100


class FuelMix:
    def __init__(self, json):
        # types
        self.types = json.get('types')
        # data
        self.data = json.get('data')

    def get_day(self) -> str:
        dayKeys = self.data.keys()
        most_recent_date_idx = datetime_helper.find_index_of_most_recent_date_str(dayKeys)
        return list(dayKeys)[most_recent_date_idx]

    def get_time(self) -> str:
        timestamp_keys = self.data[self.get_day()].keys()
        most_recent_timestamp_idx = datetime_helper.find_index_of_most_recent_date_str(timestamp_keys, DATETIME_FORMAT)
        return list(timestamp_keys)[most_recent_timestamp_idx]

    def get_current_fuel_mix(self) -> dict[str, float]:
        fuel_use = self.data[self.get_day()][self.get_time()]
        return { key: sub_dict['gen'] for key, sub_dict in fuel_use.items() }


    def get_total_generation(self) -> float:
        mix = self.get_current_fuel_mix()
        values = mix.values()
        return sum(values)

    def get_renewable_generation(self) -> float:
        mix = self.get_current_fuel_mix()
        return (mix[RenewableFuel.WIND.value] +
                mix[RenewableFuel.HYDRO.value] +
                mix[RenewableFuel.SOLAR.value] +
                mix[RenewableFuel.NUCLEAR.value] +
                mix[RenewableFuel.POWER_STORAGE.value])

    def get_renewable_percentage(self) -> float:
        return self.get_renewable_generation() / self.get_total_generation() * 100