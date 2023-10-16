"""
Excercise 10-63
Print the first 100 even numbers
"""


def main() -> None:
    for i in range(2, 201):
        if i % 2 == 0:
            print(i)
    # Note, my solution was also provided, but alternatively:
    # for i in range(2, 201, 2):
    # print(i)
    #
    # This feels the better way, due to not having to check i % 2 == 0 every 
    # (unnessecary) digit


if __name__ == "__main__":
    main()
