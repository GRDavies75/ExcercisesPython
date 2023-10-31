"""
Excercise 17-102
Check a pattern using regular expressions
"""
import re


def main() -> None:
    input_data = [
        "My favorite color is blue",
        "My shoes are blue",
        "My favorite color is red",
        "My friend's username is @blue",
        "Hello, i'm 102 years old",
    ]

    regex = re.compile("My[A-Za-z0-9 ]*blue")
    for entry in input_data:
        its_a_match = regex.match(entry)
        print(f"It's {'' if its_a_match else 'not '}a match")


if __name__ == "__main__":
    main()
