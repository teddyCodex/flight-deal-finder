import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        auth_token = os.environ.get("sheety_token")
        self.endpoint = (
            "https://api.sheety.co/d5e6515c3b402cc0e1d711818bfdacc9/flightDeals/"
        )
        self.header = {"Authorization": f"Bearer {auth_token}"}

    def get_data(self) -> dict:
        url = self.endpoint + "prices"
        response = requests.get(url=url, headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data

    def edit_row(self, data: str, row_id: int):
        url = self.endpoint + "prices/" + str(row_id)
        sheety_body = {"price": {"iataCode": data}}
        response = requests.put(url=url, headers=self.header, json=sheety_body)
        response.raise_for_status()

    def add_row(self, user_profile: dict):
        url = self.endpoint + "users"
        sheety_body = user_profile
        response = requests.post(url=url, headers=self.header, json=sheety_body)
        response.raise_for_status()
        if response.status_code == 200:
            print("Super!! You're in the club!")
