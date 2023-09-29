"""
Excercise 5-32
Flatten a list that contains lists
In other words potential inner lists should be added to 
the main list.
There could also be non-list values, so be sure to check the type
(Allthough implied) given an empty list, print an empty list

Hints:
Nested loops can be helpful
List comprehensions could be an approach
Another approach could be making use of recusrsion

Personal challenge:
Try to implement all 3 approaches (basicly 3 loops over 'input_data',
each with the suggested approach)
"""


def flatten(a_list: list[any]) -> list[any]:
    """
    resursive function:

    loops over a_list and appends the elements 1-by-1

    unless element is a (type) list then += flatten(element)
    """
    flattened_list = []
    for elem in a_list:
        # print(f"elem: {elem}")
        if isinstance(elem, list):
            # print("\trecursion")
            flattened_list += flatten(elem)
            # print(f"fl: {flattened_list}")
        else:
            flattened_list.append(elem)
            # print(f"fl: {flattened_list}")
    
    return flattened_list


def main() -> None:
    input_data = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [1, 2, 3, 4, 5, 6, [7, 8, 9]],
        [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
    ]

    # Approach 1 - nested loops
    for entry in input_data:
        output_list = []
        for elem in entry:
            if isinstance(elem, list):
                for inner_elem in elem:
                    output_list.append(inner_elem)
            else:
                output_list.append(elem)
        
        print(output_list)

    # Approach 2 - List comprehension
    # for entry in input_data:
    #     print([x if not isinstance(x, list) else x. for x in entry])
        # 
        # W.I.P. May continue first for grasping the fundamentals of
        # Generators and comprehensions
        # Given up on that idea 
        # 
        # Found the solution on the internet, hard to grasp the understanding
        # 
        # flatList = [element for innerList in inputList for element in innerList]
    
    # Approach 3 - Recursive solutionn
    for entry in input_data:
        print(f"entry: {entry} becomes:")
        print(flatten(entry))


if __name__ == "__main__":
    main()
