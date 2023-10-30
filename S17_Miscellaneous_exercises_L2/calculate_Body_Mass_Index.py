"""
Excercise 17-99
Calculate the Body Mass Index and provide category
for provided weight (kilograms) and height (cm)
BMI = kg/m^2
Categories:
Underweight < 18.5 
18.5 <= Normal < 25
25 <= Overweight < 30
Obesity >= 30
"""
import sys
sys.path.append("..")
import libs.input_library as il


def main() -> None:
    weight_in_kg = None
    height_in_cm = None
    meters_squared = None
    bmi = None
    bmi_category = None
    extra_info = [
        "Provide weight in kg and height in cm",
        "[Q = quit, W > 0.0, H > 0.0]",
    ]
    while True:
        # For readability
        print()
        user_input = il.get_user_input("For which weight (kg): ", extra_info)
        if user_input.casefold() == 'q':
            break
        weight_in_kg = il.sanetize_input_to_numerical_value(user_input)

        user_input = il.get_user_input("For which height (cm): ")
        if user_input.casefold() == 'q':
            break
        height_in_cm = il.sanetize_input_to_numerical_value(user_input)

        if not weight_in_kg or not height_in_cm:
            print("Unexpected input")
            continue

        meters_squared = (height_in_cm / 100) ** 2
        bmi = weight_in_kg / meters_squared

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
        elif bmi >= 30:
            bmi_category = "Obesity"
        
        print(f"Given height {height_in_cm:.1f} and given weight {weight_in_kg:.1f}")
        print(f"Results in a BMI of {bmi:.1f} and BMI-category of {bmi_category}")


if __name__ == "__main__":
    main()
