import os

def get_api_key(variable_name):
    """
    Retrieves the API key from the environment variable.
    Returns:
        str: API key if found, otherwise None.
    """
    api_key = os.environ.get(variable_name)
    if api_key:
        return api_key
    else:
        print("Error: API key environment variable not found.")
        return None
        
def get_openapi_key():
    return get_api_key('OPEN_API_KEY_ENV_VARIABLE')
    
def get_weatherapi_key():
    return get_api_key('WEATHER_API_KEY_ENV_VARIABLE')

# Example usage:
api_key = get_api_key()
if api_key:
    print("API key:", api_key)
