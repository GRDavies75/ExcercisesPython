"""
Excercise 4-21
Print the elements of a list followed by their indices in that list
If list is empty print "Empty list"
"""


def main() -> None:
    input_data = [
        [1,2,3,4],
        ["a","b","c","d"],
        [],
    ]

    for entry in input_data:
        if not entry:
            print("Empty List")
        for i, element in enumerate(entry):
            print(element, i)


if __name__ == "__main__":
    main()
