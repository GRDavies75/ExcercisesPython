"""
Excercise 8-50
Convert a number to the name of the season
(1 = spring...4 = winter)
If the given number is not in the range
print "enter a valid number"
"""


def main() -> None:
    input_data = [
        1,
        3,
        5,
        4,
        None,
        2,
    ]
    season_dict = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter",
    }

    for entry in input_data:
        # Cornercase
        if not entry or (entry not in season_dict):
            print("Enter a valid number")
            continue

        print(season_dict[entry])


if __name__ == "__main__":
    main()
