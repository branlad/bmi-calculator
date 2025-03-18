import pytest
from bmi_calculator import calculate_bmi

def test_bmi_underweight():
    assert calculate_bmi(5, 5, 90) == (15.3, "Underweight")

def test_bmi_underweight_upper_boundary():
    assert calculate_bmi(5, 5, 108) == (18.4, "Underweight")

def test_bmi_normal_weight_lower_boundary():
    assert calculate_bmi(5, 6, 112) == (18.5, "Normal weight")

def test_bmi_normal_weight():
    assert calculate_bmi(5, 5, 125) == (21.3, "Normal weight")

def test_normal_weight_upper_boundary():
    assert calculate_bmi(5, 5, 146.3) == (24.9, "Normal weight")

def test_bmi_overweight_lower_boundary():
    assert calculate_bmi(5, 5, 146.5) == (25.0, "Overweight")

def test_bmi_overweight():
    assert calculate_bmi(5, 5, 160) == (27.3, "Overweight")

def test_bmi_overweight_upper_boundary():
    assert calculate_bmi(5, 5, 175.5) == (29.9, "Overweight")    

def test_bmi_obese_lower_boundary():
    assert calculate_bmi(5, 5, 176) == (30.0, "Obese")

def test_bmi_obese():
    assert calculate_bmi(5, 5, 200) == (34.1, "Obese")

def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_bmi(-5, 5, 120)  # Invalid height
    with pytest.raises(ValueError):
        calculate_bmi(5, 5, -120)  # Invalid weight
