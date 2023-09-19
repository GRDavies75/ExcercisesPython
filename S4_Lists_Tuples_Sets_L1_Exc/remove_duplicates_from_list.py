"""
Excercise 4-23
Given a list, mutate the list so
the list only contains unique/distinct elements
print out the final version of the list
"""


def main() -> None:
    input_data = [
        [1,1,2,3,4,4],
        ["a","a","b","a"],
        [1,2,3],
        [],
    ]

    for entry in input_data:
        # Due note, since sets are unordered
        # No guarantee the (new) list preserves the original order
        # If order must be preserved:
        # entry = list(dict.fromkeys(entry))
        # which works since dicts are ordered by entry order
        # since python 3.5 or 3.8 
        entry = list(set(entry))
        print(entry)


if __name__ == "__main__":
    main()
