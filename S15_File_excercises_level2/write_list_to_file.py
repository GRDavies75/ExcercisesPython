"""
Excercise 15-89
Given a list, write it to a file,
with each element on a seperate line
Remember the usage of '\n'
"""


def main() -> None:
    FILE_NAME = 'list_to_file.txt'
    data = [
        "Regel 1",
        "Regel 2",
        "Regel 3",
        "Regel 4",
        "Regel 5",
    ]
       

    with open(FILE_NAME, encoding='utf-8', mode='w') as export_file:
        for elem in data:
            print(elem, file=export_file)


if __name__ == "__main__":
    main()
