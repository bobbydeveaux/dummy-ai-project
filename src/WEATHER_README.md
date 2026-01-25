# Weather Script

A Python script that fetches current weather information for any city.

## Features

- Fetch real-time weather data using OpenWeatherMap API
- Demo mode with mock data (no API key required)
- Support for multiple temperature units (Celsius, Fahrenheit, Kelvin)
- Clean, formatted output
- Comprehensive error handling

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Demo Mode (No API Key)

Run the script without an API key to use mock data:

```bash
python src/weather.py London
```

### With API Key

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and use it:

```bash
python src/weather.py "New York" YOUR_API_KEY
```

### Examples

```bash
# Demo mode
python src/weather.py Paris

# With API key
python src/weather.py Tokyo abc123def456

# Cities with spaces
python src/weather.py "San Francisco" your_api_key
```

## Output Example

```
Weather for London, GB (Demo Mode - Mock Data)
==================================================
Condition: Clear - clear sky
Temperature: 20°
Feels like: 18°
Humidity: 60%
Wind Speed: 3.5 m/s
```

## Testing

Run the test suite:

```bash
python tests/test_weather.py
```

Or use pytest:

```bash
pytest tests/test_weather.py -v
```

## API Details

The script uses the OpenWeatherMap Current Weather API. When running in demo mode (without an API key), it returns realistic mock data for testing purposes.

### Temperature Units

- `metric` - Celsius (default)
- `imperial` - Fahrenheit
- `standard` - Kelvin

## Error Handling

The script handles:
- Empty city names
- Network errors
- API errors
- Invalid responses

All errors are reported with helpful messages.

## Code Structure

- `WeatherClient` class: Main client for fetching weather data
- `get_weather()`: Fetches weather for a city
- `format_weather()`: Formats weather data for display
- `main()`: Command-line interface

## License

MIT
