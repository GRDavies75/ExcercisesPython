"""
Excercise 13-80
Count the vowels in a string recursively (case-insensitve A == a)
"""


def count_vowels(string: str) -> int:
    # Base case(s)
    if not string:
        return 0

    # to lower conversion
    lc_string = string.casefold()
        
    # recursion steps:    
    if lc_string[0] in {'a', 'e', 'i', 'o', 'u'}:
        tmp_result = 1
    else:
        tmp_result = 0

    return tmp_result + count_vowels(lc_string[1:])
    

def main() -> None:
    input_data = [
        "H",
        "Python",
        "Cake",
        "Amazing",
    ]

    for entry in input_data:
        print(count_vowels(entry))


if __name__ == "__main__":
    main()
