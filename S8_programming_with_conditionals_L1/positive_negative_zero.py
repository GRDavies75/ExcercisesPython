"""
Excercise 8-46
Given a number give back "Positive", "Negative" or "Zero"
"""


def main() -> None:
    input_data = [
        3,
        -1,
        0
    ]

    for entry in input_data:
        if entry == 0:
            print("Zero")
        elif entry > 0:
            print("Postive")
        else: # aka entry < 0
            print("Negative")


if __name__ == "__main__":
    main()
