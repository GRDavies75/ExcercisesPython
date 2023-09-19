"""
Excercise 4-22
Given a list and specific element
remove all matching elements and return a new list with the elemeent(s) removed
Print "Not found" when applicable
Print "Empty List" when applicable
"""


def main() -> None:
    input_data = [
        ([1,2,3,4], 2),
        ([3,3,2,1], 3),
        (["a","b","c","b"], "b"),
        ([3,4,5,6], 7),
        ([], 0),
    ]

    for input_list, elem_to_remove in input_data:
        # Cornercases
        if not input_list:
            print("Empty List")
            continue
        elif elem_to_remove not in input_list:
            print("Not Found")
            continue

        # Default behaviour
        output = []
        for elem in input_list:
            if elem != elem_to_remove:
                output.append(elem)
        
        print(output)


if __name__ == "__main__":
    main()
