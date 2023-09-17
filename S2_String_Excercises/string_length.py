"""
Excercise S2-1
Print the length of a string
"""


def main() -> None:
    input_data = [
        "",
        "H",
        "Hello",
        "Amazing",
    ]
    
    for input_entry in input_data:
        print(f"The length of '{input_entry}' is {len(input_entry)}")


if __name__ == "__main__":
    main()
