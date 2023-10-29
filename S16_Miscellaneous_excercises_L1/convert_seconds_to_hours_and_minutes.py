"""
Excercise 16-94
Convert seconds into minutes (int) and (also in to) hours (float)
Not covered, but I choose to integer divide to the minutes
"""


def main() -> None:
    SECONDS_IN_A_MINUTES = 60
    SECONDS_IN_A_HOUR = 3600

    input_data = [
        5400,
        7200,
        1234, 
    ]

    for entry in input_data:
        int_minutes = entry // SECONDS_IN_A_MINUTES
        float_hours = entry / SECONDS_IN_A_HOUR
        print(f"Seconds: {entry} translate to {int_minutes} minutes or {float_hours:.2f} hours")


if __name__ == "__main__":
    main()
