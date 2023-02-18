import requests

# Use IP-API service to get the user's location data based on their IP address
ip_address_url = "http://ip-api.com/json"
response = requests.get(ip_address_url)

# Check if the request was successful and parse the response data
if response.status_code == 200:
    data = response.json()
    city = data["city"]
    country_code = data["countryCode"]
    print(f"Your current location is {city}, {country_code}.")
else:
    print(f"Error: Could not retrieve location data.")
    exit()

# Use OpenWeatherMap API to get the current weather data for the user's location
api_key = "c67274d73271cdfe44de846b6197c986"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"
response = requests.get(weather_url)

# Check if the request was successful and parse the response data
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"The weather in {city} is {description} with a temperature of {temperature} Celsius.")

    if temperature < 10:
        print("It's quite cold outside. You should wear warm clothes and a coat to stay warm.")
    else:
        print("It's not too cold outside. You can wear a light jacket or sweater.")

else:
    print(f"Error: Could not retrieve weather data.")
    exit()
