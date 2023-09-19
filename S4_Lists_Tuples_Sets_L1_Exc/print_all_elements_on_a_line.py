"""
Excercise 4-18
Print all elements of a list on 1 line seperated by spaces
Or in other words, don't use the 'default' printformat of a list
"""


def main() -> None:
    input_data = [
        [3,4,5,6],
        ["a", "b", "c"],
    ]

    for entry in input_data:
        # My solution
        # ----------------------------------------
        # print(" ".join([str(x) for x in entry]))
        #
        # But it could be easier (no for loop, no conversion):
        # ----------------------------------------------------
        print(*entry, sep=" ")


if __name__ == "__main__":
    main()
