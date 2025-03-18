import pytest
from unittest.mock import patch
from bmi_cli import main

def test_valid_input(capsys):
    user_input = ["5", "5", "125"]
    
    with patch("builtins.input", side_effect=user_input):
        main()
    
    captured = capsys.readouterr()
    assert "Your BMI is 21.3. Category: Normal weight" in captured.out

def test_invalid_input_non_numeric(capsys):
    user_input = ["five", "5", "125"]
    
    with patch("builtins.input", side_effect=user_input):
        main()
    
    captured = capsys.readouterr()
    assert "Invalid input. Please enter valid numbers." in captured.out