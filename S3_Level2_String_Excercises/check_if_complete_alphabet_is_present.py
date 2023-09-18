"""
Excercise 3-10
Check if the complete alphabet is present in a string
Case-insensitive
(Western alphabet)
Spaces are ignored, if present, assume no other symbols.
"""
from string import ascii_lowercase


def main() -> None:
    input_data = [
        "abcdefghijklmnopqrstuvwxyz",
        "The quick brown fox jumps over the lazy dog",
        "Hello",
    ]
    ALPHABET = set(ascii_lowercase)

    for entry in input_data:
        lc_entry_set = set(entry.casefold())
        output = ALPHABET <= lc_entry_set
        print(f"Input: '{entry}' - Output: '{output}'")


if __name__ == "__main__":
    main()
