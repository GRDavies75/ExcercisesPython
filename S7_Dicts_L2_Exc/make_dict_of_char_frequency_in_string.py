"""
Excercise 7-43
Given a string produce a dictionary of the char frequency
Only letters are expected in the dict and use case-insensivity 
(keys are only lowercased letters, A == a)
"""


def main() -> None:
    input_data = [
        "Hello, World",
        "Excellent",
    ]

    for entry in input_data:
        char_dict = {}
        for char in entry.casefold():
            if char.isalpha():
                char_dict[char] = char_dict.get(char, 0) + 1

        print(char_dict)


if __name__ == "__main__":
    main()
