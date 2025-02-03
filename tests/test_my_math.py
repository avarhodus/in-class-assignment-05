import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2,2)
    assert res == 4

# Check for understanding
## Test difference

def test_difference():
    res = difference(2,2)
    assert res == 0

# Work together
## Test absolute sum

def test_it_should_return_positive_numbers_1():
    res = absolute_sum(-1 ,1)
    assert res == 2

def test_it_should_return_positive_numbers_2():
    res = absolute_sum(1 ,-1)
    assert res == 2

def test_it_should_return_positive_numbers_3():
    res = absolute_sum(-1 ,-1)
    #res1 = absolute_sum(1 ,1) (can combine them but its not recommended)
    assert res == 2
    #assert res1 == 2

def test_it_should_return_positive_numbers_4():
    res = absolute_sum(1 ,1)
    assert res == 2

# Check for understanding
## Test calculate age

def test_birth_year_1():
    res = calculate_birth_year(2025,20,False)
    assert res == 2004

def test_birth_year_2():
    res = calculate_birth_year(2025,20,True)
    assert res == 2005