"""
Excercise 8-47
Given a string give back:
"Empy string" when applicable
otherwise
"<char> is a <consonant|vowel>" when applicable
"<char> is not a letter" when applicable

Note: all chars are considered case-insensitive
"""


def main() -> None:
    input_data = [
        "",
        "Score: 36",
    ]
    VOWELS = "aeiou"

    for entry in input_data:
        # Cornercase
        if not entry:
            print("Empty string")
            continue

        for char in entry.casefold():
            if char.isalpha():
                if char in VOWELS:
                    print(f"{char} is a vowel")
                else:
                    print(f"{char} is a consonant")
            else:
                print(f"{char} is not a letter")


if __name__ == "__main__":
    main()
