"""
Excercise 7-41
Create a dictionary from a nested list
Assume innerlists are 'always' [value1, value2]
if there are no nested list then print an empty dictionary

I gave it my onw little spin:
an 'inner' element must be a list and of length 2 otherwise 'discard'/not added
"""


def main() -> None:
    input_data = [
        [["a", 1], ["b", 2], ["c", 3], ["d", 4]], # only original entry
        ["a", 1, ["b", 2], ["c", 3], "d", [4]], # {"b": 2, "c": 3}
        ["a", 1, ["b", 2], ["b", 3], "d", [4]], # {"b": 3}
        ["a", 1, ["b", 2], ["b", 3, 4], "d", [4]], # {"b": 2}
        [1, 2, 3], # {}
    ]

    for entry in input_data:
        new_dict = {}
        for elem in entry:
            if isinstance(elem, list) and len(elem) == 2:
                key, value = elem
                new_dict[key] = value
        
        print(new_dict)


if __name__ == "__main__":
    main()
