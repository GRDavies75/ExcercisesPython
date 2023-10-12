"""
Excercise 9-52
Print the number of days in a given month
Month name should be proper cased (start with capital)
Do not consider the concept of leap years (aka February should yield 28)
"""
import calendar as cld


def main() -> None:
    NOT_A_LEAP_YEAR = 2023

    # Do note this construct works because (default) locale is English
    # Adjust if you work with another locale
    for month_num, month_name in enumerate(cld.month_name[1:], 1):
        end_day = cld.monthrange(NOT_A_LEAP_YEAR, month_num)[1]
        print(f"{month_name} has: {end_day} days.")


if __name__ == "__main__":
    main()
