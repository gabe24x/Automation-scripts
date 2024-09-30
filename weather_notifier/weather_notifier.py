"""
Weather Notifier Application
----------------------------
A simple GUI application to fetch and display weather information using the Meteomatics API.
It allows the user to input a city name and choose how to fetch data (fixed interval or on command).
"""

from geopy.geocoders import Nominatim
from tkinter import *
import requests

# Constants for API authentication
API_USERNAME = 'your_username'
API_PASSWORD = 'your_password'
API_URL = 'https://api.meteomatics.com'


def get_coordinates(city_name):
    """Get the latitude and longitude for a given city name."""
    geolocator = Nominatim(user_agent='weather_informer')
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    else:
        print("Error: Unable to find the location.")
        return None


def weather():
    """Create and manage the main GUI window for the weather notifier."""
    master = Tk()
    master.title("Weather Notifier")
    master.geometry('400x200')  # Explicit window size for visibility

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

        print(f"Location: {location}")
        print(f"Run Mode: {'Fixed interval' if run_mode == 1 else 'On click'}")

    # Submit button
    submit_button = Button(master, text='Submit', command=on_submit)
    submit_button.grid(row=4, column=1, padx=5, pady=5)

    master.mainloop()


if __name__ == '__main__':
    weather()
