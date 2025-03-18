import pytest
from bmi_calculator import calculate_bmi

def test_bmi_underweight():
    assert calculate_bmi(5, 5, 100) == (17.0, "Underweight")

def test_bmi_normal_weight():
    assert calculate_bmi(5, 5, 125) == (21.3, "Normal weight")

def test_bmi_overweight():
    assert calculate_bmi(5, 5, 150) == (25.6, "Overweight")

def test_bmi_obese():
    assert calculate_bmi(5, 5, 180) == (30.7, "Obese")

def test_bmi_boundary_shift():
    # Introducing a 0.1 boundary shift at 18.4 instead of 18.5
    assert calculate_bmi(5, 5, 108) == (18.4, "Underweight")

def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_bmi(-5, 5, 120)  # Invalid height
    with pytest.raises(ValueError):
        calculate_bmi(5, 5, -120)  # Invalid weight
