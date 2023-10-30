"""
Excercises 16-97 & 16-98
97 = Convert Celcius to Fahrenheit
98 = Convert Fahrenheit to Celcius
(Which i find too easy, if you know the one you know the other)

So my version:
Aks user for input: Degrees (which can be a float)
Show both conversions 
Celsius in a rounded to 1 decimal float
Fahrenheit in a whole number
Based on provided degrees
"""
import sys
sys.path.append("..")
import libs.input_library as il


def convert_to_celsius(value: float) -> float:
    """
    Assuming value is a Farhenheit value
    
    Return a rounded to 1 decimal value
    """
    return round((value - 32) * 5 / 9, 1)


def convert_to_fahrenheit(value: float) -> int:
    """
    Assuming value is a Celcius value

    return a rounded whole Fahrenheit value
    """
    return int(round((value / 5 * 9 + 32),0))


def main() -> None:
    degrees = None
    celcius = None
    fahrenheit = None
    extra_information = [
        "Provide degrees for showing their",
        "(converted) Celsius or Fahrenheit values respectively",
        "[Q = quit, D >= 0.0]"
    ]

    while True:
        # For readability
        print()
        user_input = il.get_user_input("For which degrees: ", extra_information)
        if user_input.casefold() == 'q':
            break
        degrees = il.sanetize_input_to_numerical_value(user_input)
        if degrees == None: # degrees of 0 is acceptable
            print("Unexpected input")
            continue

        celcius = convert_to_celsius(degrees)
        fahrenheit = convert_to_fahrenheit(degrees)

        print(f"Given degrees: {degrees}")
        print(f"{degrees} Celcius = {fahrenheit} Fahrenheit")
        print(f"{degrees} Fahrenheit = {celcius} Celcius")


if __name__ == "__main__":
    main()
