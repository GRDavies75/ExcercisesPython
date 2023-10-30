"""
Excercise 17-100
Print a calender representation for given year and month
which both come from user input
(including error handeling and such)
"""
from calendar import TextCalendar
import sys
sys.path.append("..")
import libs.input_library as il


def main() -> None:
    year = None
    month = None
    extra_info = [
        "Display calender for certain year and month",
        "[Q = quit]",
    ]

    while True:
        # For readability
        print()
        user_input = il.get_user_input("For which year (YYYY): ", extra_info)
        if user_input.casefold() == 'q':
            break
        year = il.sanetize_input_to_numerical_value(user_input)

        user_input = il.get_user_input("For which month (1 ~ 12): ")
        if user_input.casefold() == 'q':
            break
        month = il.sanetize_input_to_numerical_value(user_input)

        if (not year or not year >= 1) or (not month or not 1 <= month <= 12):
            print("Unexpected input")
            continue

        # For readability
        print()
        tc = TextCalendar()
        # users can be 'playful' - int casting to prevent shenenigans
        print(tc.formatmonth(int(year), int(month)), end = "")


if __name__ == "__main__":
    main()
