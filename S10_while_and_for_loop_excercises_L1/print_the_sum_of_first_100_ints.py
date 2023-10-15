"""
Excercise 10-60
Print the sum of the first 100 numbers
Make use of a for loop (instead of using sum() )
"""


def main() -> None:
    result = 0
    for i in range(1, 101):
        result += i

    print(result)


if __name__ == "__main__":
    main()
