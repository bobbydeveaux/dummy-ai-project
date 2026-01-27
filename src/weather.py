"""Weather script that gets weather information for a given location."""

import requests
import sys
import json
import random
from typing import Dict, Optional


class WeatherClient:
    """Client for fetching weather information."""

    # List of cities for random selection
    DEFAULT_CITIES = [
        "London", "Paris", "Tokyo", "New York", "Sydney",
        "Berlin", "Rome", "Madrid", "Toronto", "Mumbai",
        "Dubai", "Singapore", "Amsterdam", "Seoul", "Bangkok",
        "Moscow", "Istanbul", "Cairo", "Mexico City", "Buenos Aires"
    ]

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the weather client.

        Args:
            api_key: Optional API key for OpenWeatherMap. If not provided,
                    uses a demo mode with mock data.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str, units: str = "metric") -> Dict:
        """Get current weather for a given city.

        Args:
            city: Name of the city
            units: Temperature units - 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin)

        Returns:
            Dictionary containing weather information

        Raises:
            ValueError: If city name is empty
            requests.RequestException: If the API request fails
        """
        if not city:
            raise ValueError("City name cannot be empty")

        # Demo mode - return mock data if no API key
        if not self.api_key:
            return self._get_mock_weather(city, units)

        params = {
            "q": city,
            "appid": self.api_key,
            "units": units
        }

        response = requests.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    def _get_mock_weather(self, city: str, units: str) -> Dict:
        """Return mock weather data for demo purposes.

        Args:
            city: Name of the city
            units: Temperature units

        Returns:
            Mock weather data dictionary
        """
        temp_unit = "°C" if units == "metric" else "°F" if units == "imperial" else "K"
        temp = 20 if units == "metric" else 68 if units == "imperial" else 293

        return {
            "name": city,
            "weather": [
                {
                    "main": "Clear",
                    "description": "clear sky"
                }
            ],
            "main": {
                "temp": temp,
                "feels_like": temp - 2,
                "temp_min": temp - 3,
                "temp_max": temp + 3,
                "pressure": 1013,
                "humidity": 60
            },
            "wind": {
                "speed": 3.5
            },
            "sys": {
                "country": "XX"
            },
            "mock": True  # Indicator that this is mock data
        }

    def get_random_city(self) -> str:
        """Get a random city from the default cities list.

        Returns:
            Random city name
        """
        return random.choice(self.DEFAULT_CITIES)

    def format_weather(self, weather_data: Dict) -> str:
        """Format weather data into a readable string.

        Args:
            weather_data: Weather data dictionary from get_weather()

        Returns:
            Formatted weather string
        """
        name = weather_data.get("name", "Unknown")
        country = weather_data.get("sys", {}).get("country", "")

        weather_main = weather_data.get("weather", [{}])[0].get("main", "Unknown")
        weather_desc = weather_data.get("weather", [{}])[0].get("description", "")

        main_data = weather_data.get("main", {})
        temp = main_data.get("temp", "N/A")
        feels_like = main_data.get("feels_like", "N/A")
        humidity = main_data.get("humidity", "N/A")

        wind_speed = weather_data.get("wind", {}).get("speed", "N/A")

        is_mock = weather_data.get("mock", False)
        mock_notice = " (Demo Mode - Mock Data)" if is_mock else ""

        output = f"""
Weather for {name}, {country}{mock_notice}
{'='*50}
Condition: {weather_main} - {weather_desc}
Temperature: {temp}°
Feels like: {feels_like}°
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
"""
        return output.strip()


def main():
    """Main function to run the weather script."""
    # Parse arguments
    city = None
    api_key = None

    if len(sys.argv) >= 2:
        city = sys.argv[1]
        api_key = sys.argv[2] if len(sys.argv) > 2 else None

    client = WeatherClient(api_key)

    # If no city provided, pick 20 random cities
    if not city:
        print("No city specified. Randomly selecting 20 cities...\n")

        # Select 20 random cities (without replacement)
        random_cities = random.sample(client.DEFAULT_CITIES, 20)

        # Fetch and display weather for each random city
        for idx, selected_city in enumerate(random_cities, 1):
            print(f"\n{'='*60}")
            print(f"City {idx}/20: {selected_city}")
            print('='*60)

            try:
                weather_data = client.get_weather(selected_city)
                formatted_output = client.format_weather(weather_data)
                print(formatted_output)
            except requests.RequestException as e:
                print(f"Error fetching weather data for {selected_city}: {e}", file=sys.stderr)
            except ValueError as e:
                print(f"Error for {selected_city}: {e}", file=sys.stderr)
    else:
        # Single city was specified
        try:
            weather_data = client.get_weather(city)
            formatted_output = client.format_weather(weather_data)
            print(formatted_output)
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}", file=sys.stderr)
            sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
