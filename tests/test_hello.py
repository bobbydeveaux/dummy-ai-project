"""Tests for the hello module."""

import sys
from pathlib import Path

# Add src to path so we can import the hello module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hello import hello_world


def test_hello_world_returns_message():
    """Test that hello_world returns the correct message."""
    result = hello_world()
    assert result == "Hello World"


def test_hello_world_type():
    """Test that hello_world returns a string."""
    result = hello_world()
    assert isinstance(result, str)


if __name__ == "__main__":
    # Run tests manually for verification
    print("Running test_hello_world_returns_message...")
    test_hello_world_returns_message()
    print("✓ Passed")

    print("Running test_hello_world_type...")
    test_hello_world_type()
    print("✓ Passed")

    print("\nAll tests passed!")
