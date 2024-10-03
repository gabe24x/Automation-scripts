# Weather Notifier

## Overview
This is a simple weather notifier application that gathers weather information using the Meteomatics API. It includes a graphical user interface (GUI) built with tkinter to input city names, select running modes, and display weather data.

## Setup and Installation
To set up the virtual environment and install the required Python dependencies, execute the following commands from the weather_notifier directory:
```shell
make init
source .venv/bin/activate
```

## System Dependencies
This project requires tkinter (the python3-tk package) for the GUI. If it's not already installed, you can install it using:
```shell
sudo apt-get install python3-tk
```

## Usage
Run the script from the 'weather_notifier' directory, using the command below:
```shell
make run
```

## Dependencies
* [GeoPy](https://geopy.readthedocs.io/en/stable/)
* [Requests](https://requests.readthedocs.io/)

## Example Output
When running the program, a GUI window will appear where you can:
1. Enter a city name for weather information.
2. Choose a mode to either fetch data at fixed intervals or on command.
3. View the weather information directly on the GUI.

## Clean Up
To remove the virtual environment and clean up the project directory, use:
```shell
make clean
```
