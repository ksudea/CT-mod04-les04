# Weather Forecast Application Refactored
class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}}
        
    def get_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})
    
class WeatherDataParser:
    def __init__(self, weather_data):
        self.city = weather_data["city"]
        self.temperature = weather_data["temperature"]
        self.condition = weather_data["condition"]
        self.humidity = weather_data["humidity"]
    
    def get_parsed_weather_data(self):
        return f"Weather in {self.city}: {self.temperature} degrees, {self.condition}, Humidity: {self.humidity}%"

        
class WeatherForecastApp:
    def __init__(self):
        self.weatherFetcher = WeatherDataFetcher()

    def get_detailed_forecast(self, city):
    # Function to provide a detailed weather forecast for a city
        try:
            city_weather_data = self.weatherFetcher.get_weather_data(city)
            weatherParser = WeatherDataParser(city_weather_data)
            return weatherParser.get_parsed_weather_data()
        except KeyError:
            return(f"Weather data not available for {city}")

    def display_basic_weather(self, city):
    # Function to display the basic weather forecast for a city - displays only temperature 
    # Without going through data parser
        city_weather_data = self.weatherFetcher.get_weather_data(city)
        if not city_weather_data:
            return(f"Weather data not available for {city}")
        else:
            return(f"Weather in {city}: {city_weather_data["temperature"]} degrees")