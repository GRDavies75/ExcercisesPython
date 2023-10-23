"""
Excercise 13-83
Implement a binary search recursively
Remember with Binary Search a sorted 'array' is implied
"""
from typing import Sequence


def binary_search(seq: Sequence[int], value: int, startindex: int=0) -> int:
    """
    Given an (ordered) integer Sequence seq and a searchable value

    with an eventual startindex

    return the index or -1 when not found
    """
    # Base case(s)
    if not seq:
        return -1
    else:
        length_of_sequence = len(seq)
        if length_of_sequence == 1:
            return startindex if seq[0] == value else -1
    
    # recursion steps, sequence is longer then 1 element
    middle_index = length_of_sequence // 2
    middle_value = seq[middle_index]

    if middle_value == value:
        return startindex + middle_index
    elif value < middle_value:
        return binary_search(seq[:middle_index], value, startindex)
    else: 
        split_startindex = startindex + middle_index + 1
        return binary_search(seq[middle_index + 1:], value, split_startindex)


def main() -> None:
    input_data = [
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 0),
        ([4, 5, 6, 7], 6),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
    ]

    for entry in input_data:
        int_stack, needle = entry
        print(binary_search(int_stack, needle))


if __name__ == "__main__":
    main()
