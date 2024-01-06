import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pprint import pprint

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://api.tequila.kiwi.com/"
        self.api_key: str = os.environ.get("kiwi_api")
        self.header = {"apikey": self.api_key, "accept": "application/json"}
        self.today = datetime.now()
        self.tomorrow = self.today + timedelta(1)
        self.date_from = self.tomorrow.strftime("%d/%m/%Y")
        next_six_months = self.tomorrow + timedelta(180)
        self.date_to = next_six_months.strftime("%d/%m/%Y")

    def get_IATA(self, city_name) -> str:
        url = self.endpoint + "locations/query"
        body = {"term": city_name, "location_types": "city"}
        response = requests.get(url=url, headers=self.header, params=body)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def search_flights(self, fly_from, fly_to) -> list:
        url = "https://api.tequila.kiwi.com/v2/search"
        headers = self.header
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "limit": 10,
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data["data"]
