# Proxy Weather API

A simple flask app for retrieving weather information from [OpenWeatherMap](https://openweathermap.org/) then serving as an API endpoint for client-side app. This project has been created for self-learning purposes to:

1. Learn how to serve content to client with Flask app.
2. Learn how to make requests to 3rd-party services.
3. Learn how to write robust tests.
4. Strengthen fundamental Python knowledge and a few essential libraries.

## Implementation

### Current Working-In-Progress Features

|                          API Function                           |                      Description                      |
| :-------------------------------------------------------------: | :---------------------------------------------------: |
|   [Current Weather Data](https://openweathermap.org/current)    |          Access any current location weather          |
| [5 Day / 3 Hour Forecast](https://openweathermap.org/forecast5) |   5 days forcast with 3-hour step for any location    |
|    [Geocoding](https://openweathermap.org/api/geocoding-api)    | City, areas and districts, countries and states level |

### Future Expansion (Optional)

|                         API Function                          |                                       Description                                       |
| :-----------------------------------------------------------: | :-------------------------------------------------------------------------------------: |
| [Air Pollution](https://openweathermap.org/api/air-pollution) |                   Current, forecast, and historical air polution data                   |
|                        Weather Station                        |               Connect to your own station and get aggregated measurement                |
|                        Weather Trigger                        | Generate alerts when weather conditions are met (temperature, humidity, pressure, etc.) |

## Caveats

- Request no more than once in 10 minutes for each location
- Request no more than 1,000,000 calls per month

## Notes

- Free endpoint api calls is [api.openweathermap.org](openweathermap.org), not server's IP address
- If need precise results, use [Geocoding API](openweathermap.org/api/geocoding-api)
