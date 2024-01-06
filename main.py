# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from user_manager import User
from pprint import pprint
from datetime import datetime

data_manager = DataManager()
user_manager = User(data_manager)


# flight_search = FlightSearch()


# sheet_data: list = data_manager.get_data()["prices"]


# for row in sheet_data:
#     # if iatacode column is empty, find the correct iata code and update sheet
#     if row["iataCode"] == "":
#         iata_code = flight_search.get_IATA(row["city"])
#         data_manager.edit_row(iata_code, row["id"])
#     # search for flights from london to the destination
#     else:
#         available_flights: list = flight_search.search_flights("LON", row["iataCode"])
#         flight_data_engine = FlightData(available_flights, row["lowestPrice"])
