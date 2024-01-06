from pprint import pprint
from notification_manager import NotificationManager

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, available_flights, lowest_price) -> None:
        self.available_flights = available_flights
        self.lowest_price = lowest_price
        self.get_cheapest_flight()


    def get_cheapest_flight(self):
        for flight in self.available_flights:
            if flight["price"] <= self.lowest_price:
                self.flight_profile(flight)
            else:
                return None

    def flight_profile(self, flight):
        flight_profile = {
            "price": f"￡{flight["price"]}",
            'departure_city' : flight["cityFrom"],
            'departure_airport_iata' : flight["flyFrom"],
            'arrival_city' : flight["cityTo"],
            'arrival_airport_iata' : flight["flyTo"],
            'outbound_date' : flight["local_departure"].split("T")[0],
            'inbound_date' : flight["local_arrival"].split("T")[0]
        }
        notification_engine = NotificationManager(flight_profile)

