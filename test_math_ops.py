import pytest
from math_ops import add, subtract, multiply, divide, factorial, average


class TestBasicOperations:
    """Test basic math operations"""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers"""
        assert subtract(10, 3) == 7
    
    def test_subtract_larger_from_smaller(self):
        """Test subtracting larger from smaller gives negative"""
        assert subtract(3, 10) == -7


class TestMultiplication:
    """Test multiplication operation"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers"""
        assert multiply(4, 5) == 20
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-3, -4) == 12


class TestDivision:
    """Test division operation"""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers"""
        assert divide(10, 2) == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises an error"""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


class TestFactorial:
    """Test factorial operation"""
    
    def test_factorial_of_zero(self):
        """Test factorial of 0 is 1"""
        assert factorial(0) == 1
    
    def test_factorial_of_five(self):
        """Test factorial of 5 is 120"""
        assert factorial(5) == 120
    
    def test_factorial_of_one(self):
        """Test factorial of 1 is 1"""
        assert factorial(1) == 1


class TestAverage:
    """Test average calculation"""
    
    def test_average_of_positive_numbers(self):
        """Test average of positive numbers"""
        assert average([2, 4, 6]) == 4
    
    def test_average_single_number(self):
        """Test average of single number"""
        assert average([5]) == 5
    
    def test_average_empty_list_raises_error(self):
        """Test that empty list raises an error"""
        with pytest.raises(ZeroDivisionError):
            average([])