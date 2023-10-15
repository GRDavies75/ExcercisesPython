"""
Excercise 10-59
Based on user input (assume integer >= 1)
"""


def main() -> None:
    while True:
        countdown_from = input("Please enter an integer >= 1: ")
        if countdown_from.isdigit():
            countdown_from = int(countdown_from)
            if countdown_from >= 1:
                for i in range(countdown_from, 0, -1):
                    print(i)


if __name__ == "__main__":
    main()
