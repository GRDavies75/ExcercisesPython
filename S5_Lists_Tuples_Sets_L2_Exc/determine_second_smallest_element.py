"""
Excercise 5-30
Determine second smallest element in a list
Print None if the given list is empty or contains only 1 element
Basicly the same approach as with in Exc 5-29
(Implied unique elements in a list)
So I use the suggested approach (in 5-29) which I found more elegant
"""


def main() -> None:
    input_data = [
        [1, 2, 3, 4],
        [1, 3],
        [2],
        [],
    ]

    for entry in input_data:
        if len(entry) > 1:
            sorted_list = sorted(entry)
            # second (smallest) element, 0-based indices
            print(sorted_list[1])
        else:
            print(None)


if __name__ == "__main__":
    main()
