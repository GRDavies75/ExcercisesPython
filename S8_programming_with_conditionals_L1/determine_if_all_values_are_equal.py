"""
Excercise 8-51
Determine if all 3 given values are equal

This whole conditional section rubs me wrong some how
I do understand what is meant to be done:
Confine the excercise in (hardcore) propositional logica (only)
but the beauty of Python are all the built-in functions...
As already stated by me, scalability becomes an issue 
with bigger number of variables

I will yield for this time, but would have rather used len(set(trippleVar)) == 1
"""


def main() -> None:
    input_data = [
        (3, 3, 3),
        (3, 2, 3),
        (3, 1, 7),
        (3, 3, 3),
    ]

    for entry in input_data:
        a, b, c = entry
        if a == b == c:
            print("Equal")
        else:
            print("Not equal")


if __name__ == "__main__":
    main()
