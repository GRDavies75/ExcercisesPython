"""
Excercise 3-14
Reverse words in a string
Reverse the capitalization too
Assume string only contains letters and spaces
"""


def main() -> None:
    input_data = [
        "Hello World",
        "Python is Awesome",
    ]

    for s in input_data:
        output = ""
        listed_words = s.split(" ")
        # num_of_words = len(listed_words)
        for word in listed_words:
            reversed_word = word[::-1]
            # Not knowledgable about certain functions,
            # is my only sin (in this case)
            # -----------------------------------------
            # for char in reversed_word:
            #     if char.islower():
            #         output += char.upper()
            #     else:
            #         output += char.lower()
            # 
            # There is (off course) a build-in method
            # ---------------------------------------
            swapped_case = reversed_word.swapcase()
            output += swapped_case + " "

            # Have chosen to not do a check and remove the last " " added
            # if i != num_of_words -1:
            # 
            # Funny enough this is also provided in the solution
            # extra line of code is also not needed anymore
            # output += " "

        # Correct once in the end instead of checking if it' the last word
        # As in the solution
        # 
        # 1 error, forgot about the Inmutability of strings
        # So I had to asign it instead of only using output.rstrip()
        output = output.rstrip()
    
        print(f"Input: '{s}' - Output: '{output}'")


if __name__ == "__main__":
    main()
