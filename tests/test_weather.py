"""Tests for the weather module."""

import sys
from pathlib import Path
from unittest.mock import Mock, patch
import json

# Add src to path so we can import the weather module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from weather import WeatherClient


def test_weather_client_initialization():
    """Test that WeatherClient can be initialized."""
    client = WeatherClient()
    assert client is not None
    assert client.api_key is None


def test_weather_client_with_api_key():
    """Test that WeatherClient can be initialized with an API key."""
    api_key = "test_key_123"
    client = WeatherClient(api_key)
    assert client.api_key == api_key


def test_get_weather_mock_mode():
    """Test getting weather in mock mode (no API key)."""
    client = WeatherClient()
    result = client.get_weather("London")

    assert result is not None
    assert "name" in result
    assert "weather" in result
    assert "main" in result
    assert result.get("mock") is True
    assert result["name"] == "London"


def test_get_weather_empty_city_raises_error():
    """Test that empty city name raises ValueError."""
    client = WeatherClient()
    try:
        client.get_weather("")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "City name cannot be empty" in str(e)


def test_get_weather_with_units():
    """Test getting weather with different unit systems."""
    client = WeatherClient()

    # Test metric (Celsius)
    result_metric = client.get_weather("Paris", units="metric")
    assert result_metric["main"]["temp"] == 20

    # Test imperial (Fahrenheit)
    result_imperial = client.get_weather("Paris", units="imperial")
    assert result_imperial["main"]["temp"] == 68

    # Test standard (Kelvin)
    result_standard = client.get_weather("Paris", units="standard")
    assert result_standard["main"]["temp"] == 293


def test_format_weather():
    """Test formatting weather data."""
    client = WeatherClient()
    mock_data = {
        "name": "London",
        "sys": {"country": "GB"},
        "weather": [{"main": "Cloudy", "description": "overcast clouds"}],
        "main": {
            "temp": 15,
            "feels_like": 13,
            "humidity": 75
        },
        "wind": {"speed": 5.2},
        "mock": False
    }

    formatted = client.format_weather(mock_data)

    assert "London" in formatted
    assert "GB" in formatted
    assert "Cloudy" in formatted
    assert "15" in formatted
    assert "75" in formatted


def test_format_weather_with_mock_indicator():
    """Test that mock data includes demo mode notice."""
    client = WeatherClient()
    weather_data = client.get_weather("TestCity")
    formatted = client.format_weather(weather_data)

    assert "Demo Mode" in formatted
    assert "TestCity" in formatted


@patch('weather.requests.get')
def test_get_weather_with_api_key_calls_api(mock_get):
    """Test that providing an API key calls the real API."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "name": "Berlin",
        "weather": [{"main": "Rain", "description": "light rain"}],
        "main": {"temp": 12, "feels_like": 10, "humidity": 85},
        "wind": {"speed": 4.5},
        "sys": {"country": "DE"}
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    client = WeatherClient(api_key="fake_api_key")
    result = client.get_weather("Berlin")

    assert mock_get.called
    assert result["name"] == "Berlin"
    assert result.get("mock") is None


def test_weather_data_structure():
    """Test that weather data has expected structure."""
    client = WeatherClient()
    result = client.get_weather("Tokyo")

    # Check required keys exist
    assert "name" in result
    assert "weather" in result
    assert "main" in result
    assert "wind" in result

    # Check nested structures
    assert isinstance(result["weather"], list)
    assert len(result["weather"]) > 0
    assert "main" in result["weather"][0]
    assert "description" in result["weather"][0]

    assert "temp" in result["main"]
    assert "humidity" in result["main"]
    assert "speed" in result["wind"]


def test_get_random_city():
    """Test that get_random_city returns a city from the default list."""
    client = WeatherClient()
    random_city = client.get_random_city()

    assert random_city is not None
    assert isinstance(random_city, str)
    assert len(random_city) > 0
    assert random_city in client.DEFAULT_CITIES


def test_get_random_city_multiple_calls():
    """Test that get_random_city can be called multiple times."""
    client = WeatherClient()
    cities = [client.get_random_city() for _ in range(10)]

    # All cities should be valid
    for city in cities:
        assert city in client.DEFAULT_CITIES

    # Should have at least some variation (not guaranteed, but highly likely)
    assert len(cities) == 10


def test_default_cities_list_exists():
    """Test that DEFAULT_CITIES is properly defined."""
    client = WeatherClient()

    assert hasattr(client, 'DEFAULT_CITIES')
    assert isinstance(client.DEFAULT_CITIES, list)
    assert len(client.DEFAULT_CITIES) > 0

    # All entries should be non-empty strings
    for city in client.DEFAULT_CITIES:
        assert isinstance(city, str)
        assert len(city) > 0


def test_main_without_args_selects_random_city():
    """Test that main() selects a random city when no arguments provided."""
    import weather
    import random

    # Mock sys.argv to simulate no city argument
    with patch.object(sys, 'argv', ['weather.py']):
        # Mock print to capture output
        with patch('builtins.print') as mock_print:
            # Set a seed for reproducible random selection
            random.seed(42)

            # Call main
            weather.main()

            # Get all print calls as strings
            print_calls = [str(call) for call in mock_print.call_args_list]

            # Check that "Randomly selected:" message appears
            has_random_msg = any("Randomly selected:" in str(call) for call in print_calls)
            assert has_random_msg

            # Check that a city name from DEFAULT_CITIES appears
            client = weather.WeatherClient()
            has_city = any(any(city in str(call) for city in client.DEFAULT_CITIES) for call in print_calls)
            assert has_city


def test_main_with_city_arg_uses_single_city():
    """Test that main() uses specified city when provided."""
    import weather

    # Mock sys.argv to simulate city argument
    with patch.object(sys, 'argv', ['weather.py', 'TestCity']):
        # Mock print to capture output
        with patch('builtins.print') as mock_print:
            # Call main
            weather.main()

            # Get all print calls as strings
            print_calls = [str(call) for call in mock_print.call_args_list]

            # Check that TestCity appears in output
            has_test_city = any("TestCity" in str(call) for call in print_calls)
            assert has_test_city

            # Check that we don't have random selection message
            has_random_msg = any("Randomly selected:" in str(call) for call in print_calls)
            assert not has_random_msg


if __name__ == "__main__":
    # Run tests manually for verification
    print("Running test_weather_client_initialization...")
    test_weather_client_initialization()
    print("✓ Passed")

    print("Running test_weather_client_with_api_key...")
    test_weather_client_with_api_key()
    print("✓ Passed")

    print("Running test_get_weather_mock_mode...")
    test_get_weather_mock_mode()
    print("✓ Passed")

    print("Running test_get_weather_empty_city_raises_error...")
    test_get_weather_empty_city_raises_error()
    print("✓ Passed")

    print("Running test_get_weather_with_units...")
    test_get_weather_with_units()
    print("✓ Passed")

    print("Running test_format_weather...")
    test_format_weather()
    print("✓ Passed")

    print("Running test_format_weather_with_mock_indicator...")
    test_format_weather_with_mock_indicator()
    print("✓ Passed")

    print("Running test_get_weather_with_api_key_calls_api...")
    test_get_weather_with_api_key_calls_api()
    print("✓ Passed")

    print("Running test_weather_data_structure...")
    test_weather_data_structure()
    print("✓ Passed")

    print("Running test_get_random_city...")
    test_get_random_city()
    print("✓ Passed")

    print("Running test_get_random_city_multiple_calls...")
    test_get_random_city_multiple_calls()
    print("✓ Passed")

    print("Running test_default_cities_list_exists...")
    test_default_cities_list_exists()
    print("✓ Passed")

    print("Running test_main_without_args_selects_random_city...")
    test_main_without_args_selects_random_city()
    print("✓ Passed")

    print("Running test_main_with_city_arg_uses_single_city...")
    test_main_with_city_arg_uses_single_city()
    print("✓ Passed")

    print("\nAll tests passed!")
