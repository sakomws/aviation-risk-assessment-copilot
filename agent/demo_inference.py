import random
from extract_airports import *


# Simulated local database of airport features
airport_features_db = {
    "SFO": {
        "Name": "San Francisco International Airport",
        "Location": "San Francisco, CA, USA",
        "Altitude (ft)": 13,
        "Runway Length (ft)": 11870,
        "Traffic Volume": "High",
        "Historical Incident Rate": 0.0012,  # Incidents per takeoff/landing
    },
    "JFK": {
        "Name": "John F. Kennedy International Airport",
        "Location": "New York City, NY, USA",
        "Altitude (ft)": 13,
        "Runway Length (ft)": 14572,
        "Traffic Volume": "Very High",
        "Historical Incident Rate": 0.0009,  # Incidents per takeoff/landing
    },
    "LAS": {
        "Name": "McCarran International Airport",
        "Location": "Las Vegas, NV, USA",
        "Altitude (ft)": 2181,
        "Runway Length (ft)": 14510,
        "Traffic Volume": "Very High",
        "Historical Incident Rate": 0.0005,  # Incidents per takeoff/landing
    }
}

def get_airport_features(airport_code):
    """
    Fetches airport features for a given airport code from the local database.
    
    Parameters:
    - airport_code: The code of the airport (str).
    
    Returns:
    - A dictionary containing the features of the airport.
    """
    # Fetch airport features from the local database
    features = airport_features_db.get(airport_code.upper())
    
    if features:
        return features
    else:
        return airport_features_db.get("SFO")

def estimate_risk_rate_given_airport(airport_code):
    """
    Estimates the risk rate for a given airport code based on simulated airport features.
    
    Parameters:
    - airport_code: The code of the airport (str).
    
    Returns:
    - A float representing the estimated risk rate for the airport.
    """
    # Weights for each feature (for simplicity, these are arbitrarily chosen)
    weights = {
        "Altitude (ft)": 0.1,  # Higher altitudes could imply a slight increase in risk
        "Runway Length (ft)": -0.2,  # Longer runways could imply a decrease in risk
        "Traffic Volume": {"Low": -0.1, "Medium": 0, "High": 0.2, "Very High": 0.4},  # Traffic volume increases risk
        "Historical Incident Rate": 1.0,  # Direct correlation with risk
    }

    features = get_airport_features(airport_code)
    
    # Check for error in fetching features
    if "error" in features:
        return features
    
    # Calculate risk rate based on features and weights
    risk_rate = 0.0
    risk_rate += weights["Altitude (ft)"] * features["Altitude (ft)"] / 1000  # Normalizing altitude
    risk_rate += weights["Runway Length (ft)"] * (10000 - features["Runway Length (ft)"]) / 10000  # Inverse and normalize
    traffic_volume_weight = weights["Traffic Volume"].get(features["Traffic Volume"], 0)
    risk_rate += traffic_volume_weight
    risk_rate += weights["Historical Incident Rate"] * features["Historical Incident Rate"] * 10000  # Assume per 100,000 adjusted to per 100
    
    # Ensure risk rate is within 0 to 1
    risk_rate = min(max(risk_rate, 0), 1)
    
    return risk_rate

def estimate_risk_rate_given_weather():
    return random.choice([0, 1]) / 1000




prompt_responses = {
    "bad_weather": "In bad weather, a pilot should prioritize safety above all else." + 
        " They must closely monitor weather reports and forecasts provided by the FAA,"+
        " assess the severity of the conditions, and make a decision whether to delay, "+
        "divert, or cancel the flight if conditions pose a risk to safety. Communication" +
        " with air traffic control and other relevant authorities is crucial to ensure the" +
        " best course of action is taken.",
    "risky_airport": "When operating at a high-risk airport, a pilot should meticulously "+
        "plan the flight, taking into account factors such as runway length, terrain, and weather"+
        " conditions. Prior to departure, conduct a thorough pre-flight inspection and review "+
        "emergency procedures specific to the airport. During the approach and landing phase, " + 
        "maintain heightened situational awareness, adhere strictly to established procedures, "+ 
        " and be prepared to execute a go-around or diversion if conditions deteriorate or safety is compromised.",

    "no_risk": "Good luck with your flight"
}

def estimate_risk_rates(airport_codes = ["SFO", "JFK"]):
    start_airport_risk = estimate_risk_rate_given_airport(airport_codes[0])
    end_airport_risk = estimate_risk_rate_given_airport(airport_codes[1])
    airport_risk = (start_airport_risk + end_airport_risk) / 100000
    weather_risk = estimate_risk_rate_given_weather()
    if (weather_risk > 0):
        return prompt_responses["bad_weather"]
    if (airport_risk > 0.000001):
        return prompt_responses["risky_airport"]
    
    return prompt_responses["no_risk"]


def generate_risk(prompt):
    airports = extract_airports(prompt)
    return estimate_risk_rates(airports)


print(generate_risk("flying from SFO to JFK"))

# print(estimate_risk_rates(["SFO", "JFK"]))
# print(estimate_risk_rates(["SFO", "DEN"]))
