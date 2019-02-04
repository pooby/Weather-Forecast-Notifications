# Weather-Forecast-Notifications
Provides weather forecast updates through AWS SNS

WeatherForecast.py is script that polls [OpenWeather](https://openweathermap.org/api/) to retrieve a 5-day forecast. 

Parses the JSON result for:
general weather info (rain, snow), temperature, humidity, and wind.

Then, sends the results via AWS SNS.

## Setup:
Requires:

AWS Account with IAM permissions to use SNS

boto 3 (pip install boto3)


See [AWS SDK](https://aws.amazon.com/sdk-for-python/) for more information.

### Example print results:
![forecast](https://user-images.githubusercontent.com/20694494/52232115-88517a00-2870-11e9-9979-adca6d3acbd7.png)


