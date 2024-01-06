# Flight Deals Finder Application

## Overview

The Flight Deals Finder is a comprehensive application designed to assist users in finding the best flight deals. It integrates various modules to manage flight searches, user data, flight data, and notifications.

## Modules

- **main.py**: The main script that orchestrates the functioning of the application by utilizing various modules.
- **DataManager (`data_manager.py`)**: Manages interactions with the data storage (e.g., Google Sheets), handling operations like reading and writing data.
- **FlightSearch (`flight_search.py`)**: Responsible for performing flight searches, communicating with flight APIs to fetch and filter flight information.
- **FlightData (`flight_data.py`)**: Processes and structures flight data, focusing on identifying the cheapest flight options.
- **UserManager (`user_manager.py`)**: Handles user data and interactions, including adding new users to the flight club.
- **NotificationManager (`notification_manager.py`)**: Sends out notifications to users, typically about flight deals or important updates, using services like Twilio.

## Installation

1. Clone the repository.
2. Install the required dependencies (listed in `requirements.txt`).
3. Set up environment variables for API keys and other sensitive information.

## Usage

Run `main.py` to start the application. The program will interact with the flight APIs to fetch flight details, manage user data, and send notifications about the best flight deals.

## Configuration

Ensure that all necessary API keys and environmental variables are set in `.env` file. This includes API keys for flight data and Twilio for sending notifications.

## Contributing

Contributions to enhance the application or fix issues are welcome. Please follow the standard fork-and-pull request workflow.

## License

[Specify the License here]
