"""
Excercise S02-08
Replace a character in a string
Expect always a singular char to find and to replace (no empty new_char)
Case sensitive
Print original string if no match found
"""


def main() -> None:
    input_data = [
        ("Hello", "l", "s"),
        ("World", "W", "A"),
        ("Python", "P", "x"),
        ("Python", "p", "a"),
    ]

    for s, curr_char, new_char in input_data:
        if curr_char not in s:
            print(f"Input: '{s}' - Output: '{s}'")
        else:
            # output = ""
            # My solution using range and len()
            # ---------------------------------
            # for i in range(len(s)):
            #     if s[i] == curr_char:
            #         output += new_char
            #     else:
            #         output += s[i]
            # 
            # More elegant (more Pythonic?)
            # in the provided first solution
            # ------------------------------
            # for char in s:
            #     if char == curr_char:
            #         output += new_char
            #     else:
            #         output += char
            #
            # But nothing beats the prefered usage of the string functon
            # (and probably could replace the whole if else block)
            # ----------------------------------------------------------
            output = s.replace(curr_char, new_char)

            print(f"Input: '{s}' - Output: '{output}'")


if __name__ == "__main__":
    main()
