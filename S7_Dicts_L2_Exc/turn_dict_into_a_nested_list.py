"""
Excercise 7-45
Turn a dictionary into a nested list
key is the first element in an innerlist
followed by the value
"""


def main() -> None:
    input_data = [
        {
            "description": "shoe",
            "price": 4.56,
            "color": ["red", "blue", "green"],
        },
    ]

    output_list = []
    for entry in input_data:
        for key, value in entry.items():
            inner_list = []
            inner_list.append(key)
            inner_list.append(value)
            output_list.append(inner_list)
            #
            # I thought way to difficult
            # No innerlist needed and only 1 line of code in the for loop
            # Doh! 
            # ===========================================================
            # output_list.append([key, value])

    print(output_list)


if __name__ == "__main__":
    main()
