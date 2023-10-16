"""
Excercise 10-62
Print the alphabet, uppercase and 1 letter at a time
Hint: chr() transforms unicode to a letter
65 ~ 90 are the uppercase letters
"""


def main() -> None:
    for char in range(65, 91):
        print(f"{chr(char)}")


if __name__ == "__main__":
    main()
