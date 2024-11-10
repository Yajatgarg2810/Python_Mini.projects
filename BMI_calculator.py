def bmi_calculator():
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height: "))
    unit = input("Enter unit of height (foot or cm): ")

    if unit == "foot":
        height = height * 30.48  # Convert feet to centimeters
    elif unit == "cm":
        height = height  # No conversion needed
    else:
        print("Enter valid unit:")
        return  # Exit the function if the unit is invalid

    height_meters = height / 100  # Convert centimeters to meters
    bmi = weight / (height_meters ** 2)  # Correct BMI formula
    print(f"Your BMI is {bmi:.2f}")

bmi_calculator()
