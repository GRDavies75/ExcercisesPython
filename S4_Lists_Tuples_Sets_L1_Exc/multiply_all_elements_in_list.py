"""
Excercise 4-17
Multiply all elements in a list with a fixed factor
This including the possibility that the list contains strings
Assume factor is a positive integer
"""


def main() -> None:
    input_data = [
        ([3,4,5,6], 2),
        (["a", "b", "c"], 3),
    ]

    # Forgot about 'mutability' of lists (compared to str in previous sections).
    # Technically my solution does provide the correct output
    # But the excercise specifies to multiply the elements of a list
    # which i do not do, i create another list
    # The excercise lists are very small, but my solution 'costs' double the memory
    # Which in real life situation could be a problem and is not necesary
    # -----------------------------------------------------------------------------
    # for input_list, factor in input_data:
    #     output = []
    #     for element in input_list:
    #         output.append(element * factor)
        
    #     print(output)
    for input_list, factor in input_data:
        # Note: enumerate() is faster when you want to access index & element
        # Otherwise use range(len()) if indices is all you want which is faster
        for i in range(len(input_list)):
            input_list[i] *= factor
        
        print(input_list)


if __name__ == "__main__":
    main()
