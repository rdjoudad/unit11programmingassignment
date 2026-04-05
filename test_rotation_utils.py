"""
test_rotation_utils.py
Ryma Djoudad
April 5th, 2026
Imported rotation_utils.py
Test if rotation_utils.py works as intended
"""

import pytest 
from rotation_utils import adjust_rotation

def test_hundred():
    assert adjust_rotation(100) == 100

def test_four_sixty():
    assert adjust_rotation(460) == 100

def test_eight_twenty():
    assert adjust_rotation(820) == 100

def test_negative_hundred():
    assert adjust_rotation(-100) == 260

def test_negative_four_sixty():
    assert adjust_rotation(-460) == 260

def test_negative_eight_twenty():
    assert adjust_rotation(-820) == 260

def test_wrong_input():
    with pytest.raises(TypeError):
        adjust_rotation("abc")
