"""
Weather Notifier Application
----------------------------
A simple GUI application to fetch and display weather information using the Meteomatics API.
It allows the user to input a city name and choose how to fetch data (fixed interval or on command).
"""

from geopy.geocoders import Nominatim
from tkinter import *
from datetime import datetime, timezone
import requests

# Constants for API authentication
API_USERNAME = 'universityofflorida_debrito_gabriel'
API_PASSWORD = '43PqVC1tuc'
API_URL = 'https://api.meteomatics.com'


def get_coordinates(city_name):
    """Get the latitude and longitude for a given city name."""
    geolocator = Nominatim(user_agent='weather_informer')
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    else:
        print("Error: Unable to find the location.")
        return None, None


def get_weather_data(latitude, longitude):
    """Fetch weather data using the Meteomatics API."""
    if latitude is None or longitude is None:
        return "Invalid location."

    try:
        # Get the current UTC time using timezone-aware datetime object
        current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Define the parameters for the weather request
        parameters = "t_2m:C"  # Temperature at 2 meters in Celsius
        location = f"{latitude},{longitude}"
        data_format = "json"

        # Construct the API URL with all required fields
        url = f"{API_URL}/{current_time}/{parameters}/{location}/{data_format}"

        # Make the API request
        response = requests.get(url, auth=(API_USERNAME, API_PASSWORD))

        if response.status_code == 200:
            data = response.json()
            try:
                # Parse the JSON response to extract temperature
                temperature_data = data['data']
                for parameter in temperature_data:
                    if parameter['parameter'] == 't_2m:C':
                        coordinates = parameter['coordinates'][0]
                        temperature_value = coordinates['dates'][0]['value']
                        return f"Temperature: {temperature_value}°C"
                return "Temperature data not found."
            except (IndexError, KeyError) as e:
                return "Error: Unexpected data format in API response."
        else:
            return f"Error: {response.status_code}, {response.reason}"
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"


def weather():
    """Create and manage the main GUI window for the weather notifier."""
    master = Tk()
    master.title("Weather Notifier")
    master.geometry('400x200')

    # Location input
    Label(master, text='Location:').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    location_entry = Entry(master)
    location_entry.grid(row=0, column=1, padx=5, pady=5)

    # Run interval options
    Label(master, text='Run mode:').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    run_mode_entry = IntVar()
    run_mode_entry.set(0)
    Radiobutton(master, text='Fixed interval', variable=run_mode_entry, value=1).grid(row=2, column=0, padx=5, pady=5,
                                                                                      sticky=W)
    Radiobutton(master, text='On click', variable=run_mode_entry, value=2).grid(row=3, column=0, padx=5, pady=5,
                                                                                sticky=W)

    # Submit button function
    def on_submit():
        location = location_entry.get()
        run_mode = run_mode_entry.get()

        if not location:
            print("Error: Please enter a location.")
            return

        # Get coordinates
        latitude, longitude = get_coordinates(location)

        # Get weather data
        weather_info = get_weather_data(latitude, longitude)

        # Create a new window to display the weather information
        weather_window =Toplevel(master)
        weather_window.title("Weather Information")
        weather_window.geometry('400x200')
        Label(weather_window, text=f"Location: {location}").pack(pady=10)
        Label(weather_window, text=f"Run mode: {'Fixed interval' if run_mode == 1 else 'On click'}").pack(pady=5)
        Label(weather_window, text=weather_info).pack(pady=5)

    # Submit button
    submit_button = Button(master, text='Submit', command=on_submit)
    submit_button.grid(row=4, column=1, padx=5, pady=5)

    master.mainloop()


if __name__ == '__main__':
    weather()
