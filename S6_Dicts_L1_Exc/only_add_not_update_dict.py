"""
Excercise 6-35
Given a key-value pair, only add to existing dict
if given key is already part of dict, do nothing (don't update)
"""


def main() -> None:
    # Chosen to use tuple for the key-value pair,
    # could also have been a dictionary (looping over the .items())
    input_data = [
        ({"Januari": 45, "February": 56, "March": 67}, ("April", 67)),
        ({"Januari": 45, "February": 56, "March": 67}, ("Januari", 67)),
    ]

    for init_dict, key_value_pair in input_data:
        key, value = key_value_pair
        if key not in init_dict:
            init_dict[key] = value
        
        print(init_dict)


if __name__ == "__main__":
    main()
