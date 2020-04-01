import pytest
from bmi import *


def test_convert_to_meters():
    with pytest.raises(SystemExit):
        convert_to_meters(-1, 0)
    with pytest.raises(SystemExit):
        convert_to_meters(0, 0)
    with pytest.raises(SystemExit):
        convert_to_meters(1, -1)
    with pytest.raises(SystemExit):
        convert_to_meters(1, 0)
    assert convert_to_meters(5, 6) == 1.65


def test_convert_to_kg():
    with pytest.raises(SystemExit):
        convert_to_kg(-1)
    with pytest.raises(SystemExit):
        convert_to_kg(0)
    assert convert_to_kg(1) == .45


def test_category_check():
    with pytest.raises(SystemExit):
        category_check(-1)
    with pytest.raises(SystemExit):
        category_check(0)
    assert category_check(5) == "Underweight"
    assert category_check(18.5) == "Normal"
    assert category_check(21) == "Normal"
    assert category_check(25) == "Overweight"
    assert category_check(27) == "Overweight"
    assert category_check(30) == "Obese"
    assert category_check(32) == "Obese"


def test_bmi():
    assert bmi(1, 1, 1) == 4.3, "Underweight"
