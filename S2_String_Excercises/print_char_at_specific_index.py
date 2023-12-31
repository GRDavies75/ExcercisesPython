"""
Excercise S2-2
Print the char at specific index, with some cornercases
"""


def give_indexed_char(s: str, i: int) -> str:
    """
    cornercases:

    empty string returns "Empty String"

    index i > len(s) returns "i is out of range"
    """
    # My solution
    # if s == "":
    # -----------
    # suggested solution: if not s: 
    # " if it's empty, it will result in False when checked"
    # "...and this works also on lists, tuples, dicts, etc..."
    # --------------------------------------------------------
    if not s:
        return "Empty String"
    elif len(s) < i:
        return "i is out of range"
    else:
        return(s[i])


def main() -> None:
    input_data = [
        ("Hello", 2),
        ("Pizza", 4),
        ("", 3),
        ("World", 15),
    ]

    for string, index in input_data:
        print(give_indexed_char(string, index))


if __name__ == "__main__":
    main()
