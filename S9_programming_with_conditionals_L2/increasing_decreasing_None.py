"""
Excercise 9-53
Given a sequence of numbers
Give back "<increasing order|decreasing order|None>" 
when applicable for the whole sequence

Note: the input part consists consistently of 3 numbers,
Solution provided is in spirit of the conditional nature of this section
(could have handled in a better and/or more scalable way)
"""


def main() -> None:
    input_data = [
        (1, 2, 3),
        (3, 2, 1),
        (1, 1, 1),
        (1, 2, 1),
    ]

    for entry in input_data:
        a, b, c = entry
        if a > b > c: 
            print("Decreasing Order")
        elif a < b < c: 
            print("Increasing Order")
        else:
            print(None)


if __name__ == "__main__":
    main()
