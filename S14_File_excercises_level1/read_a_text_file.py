"""
Excercise 14-84
Read from a text file
Put the contents line for line in a list
"""


def main() -> None:
    FILE_NAME = "basic_file.txt"
    file_content = []

    with open(FILE_NAME, encoding='utf-8') as text_file:
        for line in text_file:
            file_content.append(line)

    print(file_content)


if __name__ == "__main__":
    main()
