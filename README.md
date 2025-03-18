# BMI Calculator - CLI Application

## **Overview**
This is a CLI application that calculates the Body Mass Index (BMI) based on user input (height in feet and inches, and weight in pounds). The application follows a Test-Driven Development (TDD) approach and includes automated unit tests using `pytest`.

---

## **Features**
- Accepts height (feet & inches) and weight (pounds)  
- Calculates BMI and classifies into one of four categories  
- Provides validation for invalid inputs  
- Implements Weak N x 1 boundary testing  
- Includes a test suite for validation  

---

## **Installation & Setup**

### **Prerequisites**
- **OS**: Windows 10+ (or macOS/Linux)
- **Python**: Version 3.8+  
- **Dependencies**: `pytest` for testing

### **1. Clone the Repository**
```
git clone https://github.com/branlad/bmi-calculator.git
cd bmi-calculator
```

### **2. Install PyTest**
```
pip install pytest
```

## How to Run the CLI Application
```
python3 bmi_cli.py
```
Then, follow the prompts:
```
BMI Calculator
Enter height (feet): 5
Enter height (inches): 5
Enter weight (pounds): 125
Your BMI is 21.3. Category: Normal weight
```

## How to Run Tests
To run all tests, use:
```
pytest
```
or
```
pytest test_bmi_calculator.py
```
```
pytest test_bmi_cli.py
```
