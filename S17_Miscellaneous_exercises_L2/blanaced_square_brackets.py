"""
Excercise 17-103
Check if strings only containing the chars [] are balanced
Start with a opening [ and somewhere ends in a closing ]
"""


def main() -> None:
    input_data = [
        "[]",
        "][",
        "[][]",
        "][]",
        "[]][]",
        "[[[[[]]]]]",
    ]

    for entry in input_data:
        debt_counter = 0
        for char in entry:
            if char == "[":
                debt_counter += 1
            else: # char == "]"
                debt_counter -= 1
            if debt_counter < 0:
                break
        else:
            print("Balanced")
            continue

        print("Unbalanced")


if __name__ == "__main__":
    main()
