import pytest

# Function to test square
def square(n):
    return n * n


# Testing the square function
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"
    assert square(4) == 16, "Test Failed: Square of 4 should be 16"
    assert square(5) == 25, "Test Failed: Square of 5 should be 25"


# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")