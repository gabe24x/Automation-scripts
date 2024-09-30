from geopy.geocoders import Nominatim
from tkinter import *


# # # # # # # # # # # # # # # # # Constants # # # # # # # # # # # # # # # # # #
API_USERNAME = 'universityofflorida_debrito_gabriel'
API_PASSWORD = '43PqVC1tuc'
API_URL = 'https://api.meteomatics.com'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent='weather_informer')
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    else:
        return None


def weather():
    master = Tk()
    master.title("Weather Notifier")

    # Location input
    Label(master, text='Location:').grid(row=0, column=0, sticky=W)
    location_entry = Entry(master)
    location_entry.grid(row=0, column=1, sticky=W)

    # Run interval options
    Label(master, text='Run after...').grid(row=1, column=0, sticky=W)
    run_mode_entry = IntVar()
    run_mode_entry.set(0)

    Radiobutton(master, text='Fixed interval', variable=run_mode_entry, value=1).grid(row=2, column=0, sticky=W)
    Radiobutton(master, text='On click', variable=run_mode_entry, value=2).grid(row=3, column=0, sticky=W)

    # Action button
    def on_submit():
        location = location_entry.get()
        run_mode = run_mode_entry.get()

        # Print values for testing
        print(f"Location: {location}")
        print(f"Run Mode: {'Fixed interval' if run_mode == 1 else 'On click'}")

    submit_button = Button(master, text='Submit', command=on_submit)
    submit_button.grid(row=4, column=1, sticky=W)

    master.mainloop()


if __name__ == '__main__':
    weather()
