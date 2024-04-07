import requests

def get_airport_coordinates(airport_code):
    api_key = "AIzaSyBP2QBUz9THw1wRm2IOY_aZDQVMw34pXdU"
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": f"{airport_code} Airport",
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None, None

if __name__ == "__main__":
    airport_code = input("Enter the airport code: ")

    try:
        latitude, longitude = get_airport_coordinates(airport_code)
        
        if latitude is not None and longitude is not None:
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("Airport information not found.")
    except Exception as e:
        print(f"Error: {e}")