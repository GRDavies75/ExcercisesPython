"""
Excercise 9-55
Determine if a given year is a leap year
"""


def main() -> None:
    input_data = [
        2025,
        2033,
        1836,
        1912,
        2200,
    ]

    for year in input_data:
        is_leap_year = False

        if year % 400 == 0:
            is_leap_year = True
        elif year % 100 == 0:
            is_leap_year = False
        elif year % 4 == 0:
            is_leap_year = True

        print(f"{year} is{' ' if is_leap_year else ' not '}a leap year")


if __name__ == "__main__":
    main()
