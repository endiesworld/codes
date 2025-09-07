import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from src.main import classify_triangle

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, "Scalene and Right"),
    (2, 2, 2, "Equilateral"),
    (2, 2, 3, "Isosceles"),
    (1, 2, 3, "Not a triangle"),
    (5, 5, 7.07106781187, "Isosceles and Right"),
    (7, 8, 9, "Scalene"),
    (0, 0, 0, "Not a triangle"),
    (-1, 2, 2, "Not a triangle"),
    (1e10, 1e10, 1e10, "Equilateral"),
    (3, 3, 4.24264068712, "Isosceles and Right"),
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
