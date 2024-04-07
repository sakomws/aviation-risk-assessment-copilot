import requests
from airportCoordinates import *

def get_weather_data(api_key, lat, lon):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")
        return None

def get_weather_data_for_airport(airportCode):
    # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
    api_key = 'a7ae1c1af6a8440486a231626240604'
    
    airport_lat, airport_lon = get_airport_coordinates(airportCode)
    # Example airport coordinates (Denver International Airport)
#    airport_lat = 39.8560963
#    airport_lon = -104.6737371
    
    weather_data = get_weather_data(api_key, airport_lat, airport_lon)
    
    if weather_data:
        location = weather_data['location']['name']
        region = weather_data['location']['region']
        country = weather_data['location']['country']
        current = weather_data['current']
        
        print(f"Weather at {location}, {region}, {country}:")
        print(f"Condition: {current['condition']['text']}")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind Speed: {current['wind_kph']} km/h")
    else:
        print("Weather data retrieval failed.")
        
        
def main():
    # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
    api_key = 'a7ae1c1af6a8440486a231626240604'
    
    #    airport_lat, airport_lon = get_lat_long(airportCode)
    # Example airport coordinates (Denver International Airport)
    airport_lat = 39.8560963
    airport_lon = -104.6737371
    
    weather_data = get_weather_data(api_key, airport_lat, airport_lon)
    
    if weather_data:
        location = weather_data['location']['name']
        region = weather_data['location']['region']
        country = weather_data['location']['country']
        current = weather_data['current']

        print(f"Weather at {location}, {region}, {country}:")
        print(f"Condition: {current['condition']['text']}")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind Speed: {current['wind_kph']} km/h")
        print(weather_data)
    else:
        print("Weather data retrieval failed.")

if __name__ == "__main__":
    # main()
    get_weather_data_for_airport("sfo")
