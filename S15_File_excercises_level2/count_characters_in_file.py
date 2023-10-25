"""
Excercise 15-90
Count the characters in a file
Exceptions all spaces and \n
"""


def main() -> None:
    # FILE_NAME = "../S14_File_excercises_level1/sentences.txt"
    FILE_NAME = "famous_quotes.txt"
    char_count = 0
    
    with open(FILE_NAME, encoding='utf-8') as file:
        content = file.readlines()

        for line in content:
            line = line.replace(" ", "")
            line = line.strip('\n')
            char_count += len(line)
            # Note could also be method chained into a 1-liner
            # char_count += len(line.replace(" ", "").strip('\n'))

    print(char_count)


if __name__ == "__main__":
    main()
