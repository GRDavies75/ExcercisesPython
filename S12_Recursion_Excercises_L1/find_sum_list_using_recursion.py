"""
Excercise 12-73
Find the sum of a given Sequence (list, tuple) 
But making use of recursion
You may assume no shennigans, so expect always a Sequence of numbers
In case of an empty list print 0
"""
from collections.abc import Sequence


def compute_sum_recursively(sequence_var: Sequence[float]) -> float:
    """ 
    Making use of recursion to calculate the sum of a sequence of numbers
    """
    # Cornercase - empty list has been provided
    if not sequence_var:
        return 0

    # Basic step
    if len(sequence_var) == 1:
        return sequence_var[0]
    # Otherwise down the rabit hole we go
    else:
        return sequence_var[0] + compute_sum_recursively(sequence_var=sequence_var[1:])
    #
    # My code works, or better said provides the same result, BUT...
    # Funny enough, what i dedicated as the cornercase (empty list) returns 0
    # IS IN FACT the Basic Step (my Basic step could be removed)
    # The code should work too, due to the fact that slicing provides an empty sequence (so basic step == 0)
    #
    # # testing the solution using the debugger
    # return sequence_var[0] + compute_sum_recursively(sequence_var=sequence_var[1:])
    # And indeed in the last step (no [1] available, but [1:] provides an epty sequence)


def main() -> None:
    input_data = [
        [1, 2, 3],
        (4, 5, 6), # checking if tupples work too
        [-1, 2, 0],
        [0, 0, 0],
        [],
    ]

    for entry in input_data:
        print(compute_sum_recursively(entry))


if __name__ == "__main__":
    main()
