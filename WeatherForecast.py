from urllib.request import urlopen
import urllib
import json
import boto3
from datetime import datetime
import time

URL_FIVE_DAY_WEATHER = "https://api.openweathermap.org/data/2.5/forecast?q="
API_KEY = "XXXX_your api key goes here_XXXX" #See: https://openweathermap.org/api for moe information      
CITY = "Seattle"

def sendForecast():
    url = URL_FIVE_DAY_WEATHER + CITY + API_KEY
    try:
        html = urlopen(url)
    except urllib.error.HTTPError as err:
        print("Bad city!")

    byteCode = html.read()
    jsonResult = byteCode.decode("utf-8")

    json_dict = json.loads(jsonResult)
    message = "\n" + CITY + " 5-Day Weather:"

    #Parse a 5 day forecast from the API, everyday at the same time. Forecast is every 3 hours,
    #So get every 8th iteration for the same time each day (24/3 = 8)
    
    for x in range (0, 40, 8):
        weatherDetails = json_dict["list"][x]["weather"]
        weatherInfo = ""
        date = json_dict["list"][x]["dt_txt"]
        datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%a %m-%d-%Y')
        temperature = str(round((json_dict["list"][x]["main"]["temp"] * 9/5 - 459.67), 1)) + "°F"
        humidity = str(json_dict["list"][x]["main"]["humidity"]) + " %"
        wind = str(round((json_dict["list"][x]["wind"]["speed"] * 2.2369), 1)) + " mph"
        message += "\n\n\tDate: " + datetime_object
        message += "\n\tWeather:"
        for item in weatherDetails:
            message += "\n\t\t\t\t" + item["main"] + ": " + item["description"]
        message += "\n\tTemperature: " + temperature
        message += "\n\tHumidity: " + humidity
        message += "\n\tWind: " + wind

    # Create an SNS client
    sns = boto3.client('sns')
    #Publish a simple message to the specified SNS topic
    response = sns.publish(
       TopicArn= 'XXXX_put your SNS topic arn here_XXXXX',
       Message=message
    )
    
starttime=time.time()
# Send Weekly Weather Updates
# 604800 = 1 week in seconds
while True:
  sendForecast()
  time.sleep(604800.0 - ((time.time() - starttime) % 604800.0))
