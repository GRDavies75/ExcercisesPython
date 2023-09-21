"""
Excercise 5-29
Determine second largest element in a list
Print none if the given list is empty or contains only 1 element
(Not clear what to do if the list only contains mulitple same elements)

In hindsight it seems it "may be assumed, all elements are unique"
Solution (1): if len(list) > 1: sortedList[-2] (which I find a elegant solution)
Solution (2): if len(list) > 1: convert to a set, remove max and then print max
This is also a solution, but more elaborate and more implict.
"""


def main() -> None:
    input_data = [
        [1, 2, 3, 4],
        [1, 2],
        [2],
        [],
    ]

    for entry in input_data:
        # Cornercase
        if not entry:
            print(None)
            continue

        largest = None
        second_largest = None

        for elem in entry:
            if not largest or elem > largest:
                second_largest = largest
                largest = elem
        
        print(second_largest)


if __name__ == "__main__":
    main()
