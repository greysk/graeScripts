#! python3
# Prints the weather for a location from the command line
'''
Overall, the program does the following:
1. Reads the requested location from the command line
2. Downloads JSON weather data from OpenWeatherMap.org
3. Converts the string of JSON data to a Python data structure
4. Prints the weather for today and the next 2 days

The code will need to do the following:
1. Join strings in `sys.argv` to get the location.
2. Call `requests.get()` to download weather data.
3. Call `json.loads()` to convert the JSON data to a Python data structure.
4. Print the weather forcast.
'''
import json
import requests
import sys
from pathlib import Path
from datetime import datetime
# sys.argv.extend(['41.37', '-75.70'])
sys.argv.extend(['Moosic', 'PA'])


def mydata(data, path='private.dat'):
    """Access specified data from .env file."""
    path = Path(path)
    with open(path, 'r') as f:
        all = dict(tuple(line.replace('\n', '').split('='))
                   for line in f.readlines()
                   if not line.startswith('#'))
        return all[data]


BINGAPID = mydata("BINGMAPS_APPID")
WAPID = mydata("WEATHER_APPID")


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage:')
    print('\tgetOpenWeather.py city state')
    print('or')
    print('\tgetOpenWeather.py zipcode')
    sys.exit()
if len(sys.argv) == 2:
    # If only one item provided, assume it is the zip code
    city = ''
    state = '-'
    zipcode = sys.argv[1]
    location = zipcode
else:
    # Otherwise, assume city and state
    zipcode = '-'
    city = '/' + sys.argv[1]  # '/' to make url work without city
    state = sys.argv[2]
    location = f'{city.lstrip("/")}, {state}'

# Get latitude and longitude from Bing Maps API
url = (f'http://dev.virtualearth.net/REST/v1/Locations/US/{state}/{zipcode}'
       f'{city}?&key={BINGAPID}')
response = requests.get(url)
response.raise_for_status()
latlong = json.loads(response.text)
lat = round(
    latlong['resourceSets'][0]['resources'][0]['point']['coordinates'][0], 2)
long = round(
    latlong['resourceSets'][0]['resources'][0]['point']['coordinates'][1], 2)


# Download the JSON data from OpenWeatherMap.org's API.
url = ('https://api.openweathermap.org/data/2.5/onecall?lat='
       f'{lat}&lon={long}&exclude=minutely,hourly&appid={WAPID}')
response = requests.get(url)
response.raise_for_status()

# # Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions.
c = weather_data['current']
print(f'--- Weather for {location} ---')
print()
print('-- Current --')
print(f'As of {datetime.fromtimestamp(c["dt"])}:')
print('\t', c['weather'][0]['main'], '-', c['weather'][0]['description'])
print()
print('-- Forecasts --')
w = weather_data['daily']
today = w[0]['dt']
print(f'Today ({datetime.fromtimestamp(today)}):')
print('\t', w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
tomorrow = w[1]['dt']
print(f'Tomorrow ({datetime.fromtimestamp(tomorrow)}):')
print('\t', w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
dayaftmrw = w[2]['dt']
print(f'Day after tomorrow ({datetime.fromtimestamp(dayaftmrw)}):')
print('\t', w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
