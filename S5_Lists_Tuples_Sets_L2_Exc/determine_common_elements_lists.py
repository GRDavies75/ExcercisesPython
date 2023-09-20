"""
Excercise 5-28
Determine the common elements between 2 lists
Lists could be from different sizes
Print the common list (empty when applicable)
Assume all lists do have distinct values
"""


def main() -> None:
    input_data = [
        ([1,2,3], [1,2,3]),
        ([4,5,6], [1,4,5]),
        ([3,4,5], [1,2,3]),
        ([4,5,6], [1,2,3]),
    ]

    for listA, listB in input_data:
        print(list(sorted(set(listA).intersection(listB))))


if __name__ == "__main__":
    main()
