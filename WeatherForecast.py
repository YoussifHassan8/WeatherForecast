import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city_name = entry.get()
    units = units_var.get()
    api_key = "24e41723fd4f07f980670ff6298752fa"

    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": units  
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        description_label.config(text=f"Description: {weather_data['weather'][0]['description']}")
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°{get_temperature_unit(units)}")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
        pressure_label.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")

        if 'rain' in weather_data:
            if '1h' in weather_data['rain']:
                precipitation = weather_data['rain']['1h']
                precipitation_percentage = (precipitation / 10) * 100
                precipitation_label.config(text=f"Precipitation in percentage: {precipitation_percentage}%")
            else:
                precipitation_label.config(text="No precipitation data available for the last 1 hour.")
        else:
            precipitation_label.config(text="No precipitation data available.")
    else:
        # Display error message if data fetch fails
        error_message = f"Unexpected error. Status code: {response.status_code}"
        messagebox.showerror("Error", error_message)

def get_temperature_unit(units):
    if units == 'metric':
        return 'C (Celsius) - 0°C is freezing, 100°C is boiling'
    elif units == 'imperial':
        return 'F (Fahrenheit) - 32°F is freezing, 212°F is boiling'
    else:
        return 'K (Kelvin) - 0K is absolute zero, no negative values'

window = tk.Tk()
window.title("Weather Forecast")
window.geometry("600x300")

description_label = tk.Label(window, text="Description: ", font=("Arial", 12, "bold"))
description_label.place(x=10, y=50)

temperature_label = tk.Label(window, text="Temperature: ", font=("Arial", 12, "bold"))
temperature_label.place(x=10, y=70)

humidity_label = tk.Label(window, text="Humidity: ", font=("Arial", 12, "bold"))
humidity_label.place(x=10, y=90)

wind_speed_label = tk.Label(window, text="Wind Speed: ", font=("Arial", 12, "bold"))
wind_speed_label.place(x=10, y=110)

pressure_label = tk.Label(window, text="Pressure: ", font=("Arial", 12, "bold"))
pressure_label.place(x=10, y=130)

precipitation_label = tk.Label(window, text="Precipitation: ", font=("Arial", 12, "bold"))
precipitation_label.place(x=10, y=150)

greeting = tk.Label(window, text="Welcome, Please Enter Your Location: ", font=("Arial", 12, "bold"))
greeting.place(x=10, y=10)

entry = tk.Entry(window)
entry.place(x=310, y=14)

units_var = tk.StringVar()
units_var.set('metric')

units_label = tk.Label(window, text="Select Units:", font=("Arial", 10, "bold"))
units_label.place(x=310, y=50)

units_dropdown = tk.OptionMenu(window, units_var, 'metric', 'imperial', 'standard')
units_dropdown.place(x=400, y=45)

action_button = tk.Button(window, text="Search", width=10, height=0, command=get_weather)
action_button.place(x=440, y=10)

window.mainloop()