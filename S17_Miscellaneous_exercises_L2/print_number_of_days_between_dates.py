"""
Excercise 17-101
Find the number of days between two dates
Both dates must be from user input YYYY MM DD
Original excercise ask for the space ' ' as seperator
My version:
Let's be user friendly, if the user is consistent create date
eg 2023-10-31 or 2020/04/03 or 2000 01 02 etc
and this is per date individualy (first- and second date can have different seperators)
Extra challenge in the prompt give 2 different examples (eg YYYY/MM/DD and 1975 08 27)

Original does not mention any error handling, assume user is benevolent and doesn't insert 
non-convertable to date input. Program may crash. 
"""
import sys
sys.path.append("..")
import libs.input_library as il
import random
from datetime import date


def generate_two_date_examples() -> tuple[str, str]:
    the_seperators = [
        "/",
        "-",
        " ",
    ]
    examples_of_seperators = random.sample(the_seperators, 2)
    first_seperator = examples_of_seperators[0]
    second_seperator = examples_of_seperators[1]
    generic_date_parts = [
        "YYYY",
        "MM",
        "DD",
    ]
    first_example = first_seperator.join(generic_date_parts)
    random_year = random.randint(1900, 2099)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28) # to guarantee a valid date
    second_example = f"{random_year}{second_seperator}{random_month:0>2}{second_seperator}{random_day:0>2}"

    return (first_example, second_example)


def convert_to_date(string: str) -> date|None:
    """
    convert a string (YYYYxMMxDD) to a date

    where x is a consistent seperator (non-digit char)

    return None if conversion was not possible
    """
    numbers = { str(x) for x in range(0, 10) }
    input_set = set(string)
    input_set -= numbers
    if len(input_set) != 1:
        return None
    year, month, day = [ int(p) for p in string.split(input_set.pop()) ]

    return date(year, month, day)


def main() -> None:
    while True:
        first_date_example, second_date_example = generate_two_date_examples()
        extra_information = [
            f"Calculate the difference in days between 2 dates {first_date_example}",
            f"Be consistent with the seperator, eg {second_date_example}",
            "[Q = quit, Date 1 <= Date 2]",
        ]
        # For readability
        print()
        user_input = il.get_user_input("Date 1: ", extra_information)
        if user_input.casefold() == 'q':
            break
        first_date = convert_to_date(user_input)

        user_input = il.get_user_input("Date 2: ")
        if user_input.casefold() == 'q':
            break
        second_date = convert_to_date(user_input)

        if not first_date or not second_date or first_date > second_date:
            print("Please enter valid dates")
            continue

        difference = second_date - first_date
        if difference.days == 0:
            print("The dates are equal")
        else:
            print(f"The dates differ {difference.days} day(s)")
        

if __name__ == "__main__":
    main()
