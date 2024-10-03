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
API_USERNAME = 'uf_debrito_gabe'
API_PASSWORD = '0XTgeIb5r6'
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
        # Get the current UTC time using datetime object
        current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Parameters for the weather request
        parameters = "t_2m:C,t_max_2m_24h:C,t_min_2m_24h:C,wind_speed_10m:ms,wind_dir_10m:d,precip_24h:mm,msl_pressure:hPa,uv:idx"
        location = f"{latitude},{longitude}"
        data_format = "json"

        # Construct the API URL with all required fields
        url = f"{API_URL}/{current_time}/{parameters}/{location}/{data_format}"

        # Make API request
        response = requests.get(url, auth=(API_USERNAME, API_PASSWORD))

        if response.status_code == 200:
            data = response.json()
            weather_info = []

            # Parse the JSON response to extract the required weather information
            try:
                for parameter in data['data']:
                    param_name = parameter['parameter']
                    param_value = parameter['coordinates'][0]['dates'][0]['value']

                    # Map the parameter names to human-readable text
                    if param_name == 't_2m:C':
                        weather_info.append(f"Temperature: {param_value}°C")
                    elif param_name == 't_max_2m_24h:C':
                        weather_info.append(f"Max Temperature (24h): {param_value}°C")
                    elif param_name == 't_min_2m_24h:C':
                        weather_info.append(f"Min Temperature (24h): {param_value}°C")
                    elif param_name == 'wind_speed_10m:ms':
                        weather_info.append(f"Wind Speed: {param_value} m/s")
                    elif param_name == 'wind_dir_10m:d':
                        weather_info.append(f"Wind Direction: {param_value}°")
                    elif param_name == 'precip_24h:mm':
                        weather_info.append(f"Precipitation (24h): {param_value} mm")
                    elif param_name == 'msl_pressure:hPa':
                        weather_info.append(f"Pressure: {param_value} hPa")
                    elif param_name == 'uv:idx':
                        weather_info.append(f"UV Index: {param_value}")

                # Join all the weather information into a single string
                return '\n'.join(weather_info)

            except (IndexError, KeyError):
                return "Error: Unexpected data format in API response."
        else:
            return f"Error: {response.status_code}, {response.reason}"
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"


def weather():
    """Create and manage the main GUI window for the weather notifier."""
    master = Tk()
    master.title("Weather Notifier")
    master.geometry('325x175')

    # Location input
    Label(master, text='Location:').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    location_entry = Entry(master)
    location_entry.grid(row=0, column=1, padx=5, pady=5)

    # Run interval options
    Label(master, text='Run mode:').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    run_mode_entry = IntVar()
    run_mode_entry.set(0)
    Radiobutton(master, text='Fixed interval', variable=run_mode_entry, value=1).grid(row=2, column=0, padx=5, pady=5, sticky=W)
    Radiobutton(master, text='On click', variable=run_mode_entry, value=2).grid(row=3, column=0, padx=5, pady=5, sticky=W)

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
        weather_window = Toplevel(master)
        weather_window.title("Weather Information")
        weather_window.geometry('400x300')
        weather_window.resizable(True, True)
        weather_window.grid_rowconfigure(0, weight=1)
        weather_window.grid_columnconfigure(0, weight=1)

        # Create labels and center them
        Label(weather_window, text=f"Location: {location}").grid(row=0, pady=10, sticky='nsew')
        Label(weather_window, text=f"Run mode: {'Fixed interval' if run_mode == 1 else 'On click'}").grid(row=1, pady=5, sticky='nsew')
        weather_label = Label(weather_window, text=weather_info, justify=CENTER)
        weather_label.grid(row=2, column=0, pady=5, sticky='nsew')

        def on_update():
            # Update the weather information
            new_weather_info = get_weather_data(latitude, longitude)
            weather_label.config(text=new_weather_info)

        if run_mode == 1:
            # On click run mode
            def periodic_update():
                on_update()
                weather_window.after(300000, periodic_update)  # Update every 5 minutes
            periodic_update()
        else:
            # Fixed interval run mode
            update_button = Button(weather_window, text='Update weather info', command=on_update)
            update_button.grid(row=3, column=0, padx=5, pady=20, sticky='nsew')

    # Submit button
    submit_button = Button(master, text='Submit', command=on_submit)
    submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

    master.mainloop()


if __name__ == '__main__':
    weather()
