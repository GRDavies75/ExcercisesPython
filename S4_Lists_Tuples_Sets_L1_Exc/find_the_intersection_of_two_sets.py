"""
Excercise 4-25
Determine the intersection of set1 & set2 and put it into a seperate set
Print the set or print an empty set when there is no intersection
"""


def main() -> None:
    input_data = [
        ({1,2,3}, {4,5,6}),
        ({1,2,3}, {3,4,5}),
        ({1,2,3,4}, {3,4,5,6}),
        ({1,2,3,4}, {1,2,3,4}),
    ]

    for set1, set2 in input_data:
        print(set1.intersection(set2))


if __name__ == "__main__":
    main()
