"""Script to output random words."""

import random


class RandomWordGenerator:
    """Generator for random words."""

    # A diverse list of words for random selection
    WORD_LIST = [
        "apple", "banana", "cherry", "dragon", "elephant",
        "forest", "garden", "harmony", "island", "jungle",
        "keyboard", "lantern", "mountain", "nature", "ocean",
        "pyramid", "quantum", "rainbow", "sunset", "thunder",
        "umbrella", "village", "waterfall", "xenon", "yellow",
        "zebra", "anchor", "butterfly", "cascade", "diamond",
        "eclipse", "flamingo", "glacier", "horizon", "infinity",
        "jasmine", "kaleidoscope", "lighthouse", "meadow", "nebula",
        "oasis", "pavilion", "quartz", "river", "sapphire",
        "telescope", "universe", "volcano", "whisper", "xylophone"
    ]

    def __init__(self):
        """Initialize the random word generator."""
        pass

    def generate_words(self, count: int = 10) -> list:
        """Generate a list of random words.

        Args:
            count: Number of words to generate (default: 10)

        Returns:
            List of random words

        Raises:
            ValueError: If count is not positive or exceeds available words
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer")

        if count > len(self.WORD_LIST):
            raise ValueError(f"Count cannot exceed {len(self.WORD_LIST)} (available words)")

        return random.sample(self.WORD_LIST, count)

    def print_words(self, words: list) -> None:
        """Print words to stdout.

        Args:
            words: List of words to print
        """
        for idx, word in enumerate(words, 1):
            print(f"{idx}. {word}")


def main():
    """Main function to run the random words script."""
    generator = RandomWordGenerator()

    # Generate 30 random words
    words = generator.generate_words(30)

    print("30 Random Words:")
    print("=" * 30)
    generator.print_words(words)


if __name__ == "__main__":
    main()
