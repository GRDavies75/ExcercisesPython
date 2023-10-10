"""
Excercise 8-48 
Give back the maximum of 3 integers

Have mixed feelings about this one.
This should be about conditionals, but in the example it is shown as a tuple
Which is I believe a iterable and there is also the max() build in function...
...
In the spirit of the excercise probably an 2 layered if then else?
UPDATE: sort of: if a > b and a > c elif same for b else c. ... 
within the excercise would be acceptable, but definitly not scalable...
"""


def main() -> None:
    input_data = [
        (1, 2, 3),
        (7, 2, 15),
        (3, 3, 3),
    ]

    for entry in input_data:
        print(f"{max(entry)}")


if __name__ == "__main__":
    main()
