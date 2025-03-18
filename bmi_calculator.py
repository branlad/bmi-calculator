def calculate_bmi(feet: int, inches: int, weight_pounds: float) -> tuple[float, str]:
    if feet < 0 or inches < 0 or weight_pounds <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    
    # Convert height to inches
    total_inches = (feet * 12) + inches
    height_meters = total_inches * 0.025
    weight_kg = weight_pounds * 0.45
    
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    bmi = round(bmi, 1)  # Smallest allowable change is 0.1

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category
