import requests
import json

# api and url support
API_KEY = "7d3619b1f06955175e9534c81907cd64"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# getting city input from user
city = input("Enter a city name : ")

# constructing the full API request URL
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
"""
1. f"...": The f at the beginning tells Python that this is a formatted string, which means any variables inside curly braces {} should be replaced with their 
actual values.

2. {BASE_URL}: This is the first part of the URL. The code replaces {BASE_URL} with the value of the BASE_URL variable, which is 
"http://api.openweathermap.org/data/2.5/weather". This is the fundamental endpoint for getting current weather data.

3. ?: The question mark is a standard part of URLs. It separates the main URL from the query parameters that follow. Query parameters are used to send specific 
information to the server.

4. q={city}: This is the first query parameter, q stands for "query." For the OpenWeatherMap API, it's used to specify the location you want weather for.
{city} is replaced by whatever the user typed in and was stored in the city variable (e.g., "London").So, this part becomes q=London.

5. &: The ampersand is used to separate multiple query parameters from each other.

6. appid={API_KEY}: This is the second query parameter, required for authentication, appid stands for "Application ID." {API_KEY} is replaced by the value of your 
API_KEY variable. This tells the server who is making the request.

7. &units=metric: This is the third query parameter, units specifies the unit system for the results, By setting it to metric, you're asking the API to return the 
temperature in Celsius, wind speed in meters per second.
"""

try:
    response = requests.get(request_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

    # The response from the API is in JSON format. We need to parse it into a Python dictionary.
    # data is now dictionary
    data = response.json()

    # Extract the relevant weather information, JSON response.
    weather_description = data['weather'][0]['description']

    temperature = data['main']['temp']

    humidity = data['main']['humidity']

    wind_speed = data['wind']['speed']
    wind_direction = data['wind']['deg']  # Wind direction in degrees
    visibility = data['visibility'] # visiblity in meters


    # --- Display the weather information ---
    print(f"\nWeather Report for {city.capitalize()}:")
    print("-" * 30)
    print(f"Description:     {weather_description.capitalize()}")
    print(f"Temperature:     {temperature}°C")
    print(f"Humidity:        {humidity}%")
    print(f"Wind:            {wind_speed * 18/5} km/hr at {wind_direction}°")
    print(f"Visibility:      {visibility / 1000} km") # Convert meters to kilometers
    print("-" * 30)

except requests.exceptions.HTTPError as errh:
    print(f"Http Error: {errh}")

except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")

except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")

except requests.exceptions.RequestException as err:
    print(f"Oops: Something Else: {err}")
    
except KeyError:
    print("Could not find weather data for that city. Please check the spelling.")