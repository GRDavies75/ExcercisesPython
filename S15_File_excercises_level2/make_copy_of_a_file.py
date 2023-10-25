"""
Excercise 15-91
Make a (exact) copy of a file
"""


def main() -> None:
    READ_FILE = "famous_quotes.txt"
    WRITE_FILE = "famous_quotes_copy.txt"
    content = None

    with open(READ_FILE, mode='r', encoding='utf-8') as read_file:
        content = read_file.readlines()

    with open(WRITE_FILE, mode='w', encoding='utf-8') as write_file:
        for line in content:
            write_file.write(line)

    # apparently you can also open multiple files at once
    # 
    # Not my code
    # ------------------------------------------------------------
    # 
    # with open(READ_FILE) as file, open(WRITE_FILE, 'w') as copy:
    #     for line in file:
    #         copy.write(line)


if __name__ == "__main__":
    main()
