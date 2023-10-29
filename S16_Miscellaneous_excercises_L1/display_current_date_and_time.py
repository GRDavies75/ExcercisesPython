"""
Excercise 16-93
Display the current date & time
"""
from datetime import datetime as dt


def main() -> None:
    nu_nu = dt.now()
    print("Current date and time:")
    print(dt.strftime(nu_nu, "%Y/%m/%d %H:%M:%S"))


if __name__ == "__main__":
    main()
