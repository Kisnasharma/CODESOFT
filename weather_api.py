import requests
import tkinter as tk
from tkinter import messagebox

# API details
API_KEY = "7d3619b1f06955175e9534c81907cd64"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()

        # Extract details
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']
        visibility = data['visibility']

        # Update result label
        result_text.set(
            f"Weather Report for {city.capitalize()}:\n"
            f"------------------------------\n"
            f"Description:   {weather_description.capitalize()}\n"
            f"Temperature:   {temperature}°C\n"
            f"Humidity:      {humidity}%\n"
            f"Wind:          {round(wind_speed * 18/5, 2)} km/hr at {wind_direction}°\n"
            f"Visibility:    {visibility / 1000} km\n"
            f"------------------------------"
        )

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")

    except KeyError:
        messagebox.showerror("Error", "City not found! Please check spelling.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Input
tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=25, justify="center")
city_entry.pack(pady=5)

# Button
tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=get_weather).pack(pady=10)

# Result area
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 11), bg="white", fg="black", relief="solid", justify="left", wraplength=350)
result_label.pack(pady=10, padx=10, fill="both", expand=True)

root.mainloop()
