import pytest
from my_math import *

def test_add():
    calculator = MathOperations(2,3)
    assert calculator.add() == 5
    
def test_sub():
    calculator = MathOperations(2,3)
    assert calculator.sub() == -1
    
def test_mult():
    calculator = MathOperations(2,3)
    assert calculator.mult() == 6
    
def test_div():
    calculator = MathOperations(2,2)
    assert calculator.div() == 1