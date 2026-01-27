"""Tests for the random_words module."""

import sys
from pathlib import Path

# Add src to path so we can import the random_words module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from random_words import RandomWordGenerator


def test_generate_words_default_count():
    """Test that generate_words returns 10 words by default."""
    generator = RandomWordGenerator()
    words = generator.generate_words()
    assert len(words) == 10


def test_generate_words_custom_count():
    """Test that generate_words returns the specified number of words."""
    generator = RandomWordGenerator()
    words = generator.generate_words(5)
    assert len(words) == 5


def test_generate_words_returns_list():
    """Test that generate_words returns a list."""
    generator = RandomWordGenerator()
    words = generator.generate_words(10)
    assert isinstance(words, list)


def test_generate_words_returns_strings():
    """Test that all generated words are strings."""
    generator = RandomWordGenerator()
    words = generator.generate_words(10)
    assert all(isinstance(word, str) for word in words)


def test_generate_words_unique():
    """Test that generated words are unique (no duplicates)."""
    generator = RandomWordGenerator()
    words = generator.generate_words(10)
    assert len(words) == len(set(words))


def test_generate_words_from_word_list():
    """Test that generated words come from the WORD_LIST."""
    generator = RandomWordGenerator()
    words = generator.generate_words(10)
    assert all(word in generator.WORD_LIST for word in words)


def test_generate_words_invalid_count_zero():
    """Test that generate_words raises ValueError for count=0."""
    generator = RandomWordGenerator()
    try:
        generator.generate_words(0)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "positive integer" in str(e)


def test_generate_words_invalid_count_negative():
    """Test that generate_words raises ValueError for negative count."""
    generator = RandomWordGenerator()
    try:
        generator.generate_words(-5)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "positive integer" in str(e)


def test_generate_words_exceeds_available():
    """Test that generate_words raises ValueError when count exceeds available words."""
    generator = RandomWordGenerator()
    try:
        generator.generate_words(1000)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "cannot exceed" in str(e)


def test_word_list_not_empty():
    """Test that WORD_LIST is not empty."""
    generator = RandomWordGenerator()
    assert len(generator.WORD_LIST) > 0


def test_word_list_has_enough_words():
    """Test that WORD_LIST has at least 10 words."""
    generator = RandomWordGenerator()
    assert len(generator.WORD_LIST) >= 10


if __name__ == "__main__":
    # Run tests manually for verification
    print("Running test_generate_words_default_count...")
    test_generate_words_default_count()
    print("✓ Passed")

    print("Running test_generate_words_custom_count...")
    test_generate_words_custom_count()
    print("✓ Passed")

    print("Running test_generate_words_returns_list...")
    test_generate_words_returns_list()
    print("✓ Passed")

    print("Running test_generate_words_returns_strings...")
    test_generate_words_returns_strings()
    print("✓ Passed")

    print("Running test_generate_words_unique...")
    test_generate_words_unique()
    print("✓ Passed")

    print("Running test_generate_words_from_word_list...")
    test_generate_words_from_word_list()
    print("✓ Passed")

    print("Running test_generate_words_invalid_count_zero...")
    test_generate_words_invalid_count_zero()
    print("✓ Passed")

    print("Running test_generate_words_invalid_count_negative...")
    test_generate_words_invalid_count_negative()
    print("✓ Passed")

    print("Running test_generate_words_exceeds_available...")
    test_generate_words_exceeds_available()
    print("✓ Passed")

    print("Running test_word_list_not_empty...")
    test_word_list_not_empty()
    print("✓ Passed")

    print("Running test_word_list_has_enough_words...")
    test_word_list_has_enough_words()
    print("✓ Passed")

    print("\nAll tests passed!")
