"""
Excercise 3-10
Check if the complete alphabet is present in a string
Case-insensitive
(Western alphabet)
Spaces are ignored, if present, assume no other symbols.
"""
import string


def main() -> None:
    input_data = [
        "abcdefghijklmnopqrstuvwxyz",
        "The quick brown fox jumps over the lazy dog",
        "Hello",
    ]
    ALPHABET = set(string.ascii_lowercase)

    for entry in input_data:
        lc_entry_set = set(entry.casefold())
        # discard any potential space (" ")
        lc_entry_set.discard(" ")
        # Sets do have distinct values, so basicly the sets should be the same to pass
        output = ALPHABET == lc_entry_set
        print(f"Input: '{entry}' - Output: '{output}'")


if __name__ == "__main__":
    main()
