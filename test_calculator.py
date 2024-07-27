import pytest # Import pytest
from calculator import calculator # Import the calculator function from calculator.py

'''NOTE: 
The assert statement is used to check if the output of the function is as expected.
The pytest.approx function is used to compare floating point numbers.
The with word is commonly used to catch exceptions in Python.
'''

# 1. Normal Operations

def test_addition(): # This function tests the addition operation.
    assert calculator(5, 3, 'add') == 8
    assert calculator(5, -3, 'add') == 2
    assert calculator(-5, -3, 'add') == -8
    assert pytest.approx(calculator(2.5, 3.7, 'add')) == 6.2 # Use pytest.approx to compare floating point numbers

def test_subtraction(): # This function tests the subtraction operation.
    assert calculator(8, 3, 'subtract') == 5
    assert calculator(3, 8, 'subtract') == -5
    assert calculator(5, -3, 'subtract') == 8
    assert pytest.approx(calculator(5.5, 3.2, 'subtract')) == 2.3

def test_multiplication(): # This function tests the multiplication operation.
    assert calculator(4, 3, 'multiply') == 12
    assert calculator(4, -3, 'multiply') == -12
    assert calculator(-4, -3, 'multiply') == 12
    assert pytest.approx(calculator(2.5, 3.0, 'multiply')) == 7.5

def test_division(): # This function tests the division operation.
    assert calculator(10, 2, 'divide') == 5
    assert pytest.approx(calculator(2, 10, 'divide')) == 0.2
    assert calculator(6, -3, 'divide') == -2
    assert pytest.approx(calculator(5.0, 2.0, 'divide')) == 2.5

# 2. Edge Cases

def test_edge_cases():
    assert calculator(5, 0, 'add') == 5
    assert calculator(5, 0, 'subtract') == 5
    assert calculator(5, 0, 'multiply') == 0
    assert calculator(5, 1, 'divide') == 5
    assert calculator(0, 5, 'divide') == 0

# 3. Error Handling
def test_divide_by_zero_error():
    with pytest.raises(ValueError):
        calculator(5, 0, 'divide')

def test_invalid_operation():
    with pytest.raises(ValueError):
        calculator(5, 5, 'calculate')

# 4. Large Numbers

def test_large_numbers():
    assert calculator(1000000, 2000000, 'add') == 3000000
    assert calculator(100000, 100000, 'multiply') == 10000000000

# 5. Precision

def test_precision():
    assert pytest.approx(calculator(1, 3, 'divide'), rel=1e-15) == 0.3333333333333333 # Use the rel parameter to set the relative tolerance
    assert pytest.approx(calculator(0.1, 0.2, 'add'), rel=1e-15) == 0.3