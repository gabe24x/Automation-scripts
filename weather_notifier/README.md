# Weather Notifier

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```shell
user@computer:~$ make init
user@computer:~$ source .venv/bin/activate
```

## Overview
This is a simple weather notifier application that gathers weather information using the Meteomatics API. It includes a graphical user interface (GUI) built with tkinter to input city names, select running modes, and display weather data.

## Usage
Run the script using the command below:
```shell
user@computer:~$ make run
```
Alternatively, you can directly execute the Python script:
```shell
user@computer:~$ python3 weather.py
```

## Example Output
When running the program, a GUI window will appear where you can:
1. Enter a city name for weather information.
2. Choose a mode to either fetch data at fixed intervals or on command.
3. View the weather information directly on the GUI.

### Dependencies
* [GeoPy](https://geopy.readthedocs.io/en/stable/)
