import re

def extract_airports(pattern):
    match = re.match(r'flying from (\w+) to (\w+)', pattern, re.IGNORECASE)
    if match:
        start_airport = match.group(1).upper()
        end_airport = match.group(2).upper()
        return [start_airport, end_airport]
    else:
        return [None, None]