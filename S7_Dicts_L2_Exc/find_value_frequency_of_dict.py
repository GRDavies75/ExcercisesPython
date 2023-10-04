"""
Excercise 7-40
Create a dictionary with the frequency of values of an other dict
Print an empty dict if other is also empty
"""


def main() -> None:
    input_data = [
        {
            "a": 4,
            "b": 4,
            "c": 2,
            "d": 7,
            "e": 4,
            "f": 2,
            "g": 7,
            "h": 7,
        },
        {}
    ]

    for entry in input_data:
        freq_dict = {}
        for value in entry.values():
            freq_dict[value] = freq_dict.get(value, 0) + 1
        
        print(freq_dict)


if __name__ == "__main__":
    main()
