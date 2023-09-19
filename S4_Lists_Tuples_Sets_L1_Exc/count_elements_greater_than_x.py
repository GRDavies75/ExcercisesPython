"""
Excercise 4-23
Count elements greater then 3 (or X)
Assume list contain only numbers (integers?)
Print the final count
"""


def main() -> None:
    input_data = [
        [1,-1,0,2,2,3],
        [1,2,3,4],
        [7,8,9,10],
        [],
    ]
    CUT_OFF = 3

    for entry in input_data:
        print(len([x for x in entry if x > CUT_OFF]))
        # alternatively
        # print(sum(1 for x in entry if x > CUT_OFF))


if __name__ == "__main__":
    main()
