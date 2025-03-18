from bmi_calculator import calculate_bmi

def main():
    print("BMI Calculator")
    
    try:
        feet = int(input("Enter height (feet): "))
        inches = int(input("Enter height (inches): "))
        weight = float(input("Enter weight (pounds): "))

        bmi, category = calculate_bmi(feet, inches, weight)
        print(f"Your BMI is {bmi}. Category: {category}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
