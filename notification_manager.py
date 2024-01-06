import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_profile: dict) -> None:
        self.twilio_sid = os.environ.get("twilio_sid")
        self.twilio_auth = os.environ.get("twilio_auth")
        self.flight_profile = flight_profile
        self.format_sms()

    def format_sms(self):
        sms = f"Low price alert! Only {self.flight_profile['price']} to fly from {self.flight_profile['departure_city']}-{self.flight_profile['departure_airport_iata']} to {self.flight_profile['arrival_city']}-{self.flight_profile['arrival_airport_iata']} from {self.flight_profile['outbound_date']}"
        self.send_sms(sms=sms)

    def send_sms(self, sms):
        sender = "+17816077046"
        receiver = "+2349139390731"
        client = Client(self.twilio_sid, self.twilio_auth)
        message = client.messages.create(from_=sender, to=receiver, body=sms)
        print(message.sid)
