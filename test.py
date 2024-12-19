import pytest

# Function to test the core logic of app.py
def calculate_powers(n):
    square = n ** 2
    cube = n ** 3
    fifth_power = n ** 5
    return square, cube, fifth_power

def test_calculate_powers():
    # Test for n = 2
    n = 2
    square, cube, fifth_power = calculate_powers(n)
    assert square == 4
    assert cube == 8
    assert fifth_power == 32

    # Test for n = -3
    n = -3
    square, cube, fifth_power = calculate_powers(n)
    assert square == 9
    assert cube == -27
    assert fifth_power == -243

    # Test for n = 0
    n = 0
    square, cube, fifth_power = calculate_powers(n)
    assert square == 0
    assert cube == 0
    assert fifth_power == 0
