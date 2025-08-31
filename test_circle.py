import circle
import pytest
import math
from circle import Circle

def test_getRadius():
    #creating my circle obj
    circ= Circle(4)
    radius = circ.getRadius()
    assert radius == 4

def test_setRadius_pos():
    circ = Circle(4)
    changed = circ.setRadius(8)
    radius = circ.getRadius()
    assert radius == 8
    assert changed == True

def test_setRaduis_neg():
    circ = Circle(4)
    changed = circ.setRadius(-1)
    radius = circ.getRadius()
    assert radius == 4
    assert changed == False

def test_getArea_ret_zero():
    circ = Circle(2)
    area = circ.getArea()
    assert area == 0

def test_getArea_reg():
    circ= Circle(4)
    area = circ.getArea()
    calc = math.pi * 4 * 4
    assert calc == area

def test_getArea_zero():
    circ = Circle(0)
    area = circ.getArea()
    calc = math.pi * 0 * 0
    assert calc == area

def test_getCircumference():
    circ = Circle(4)
    cumfrence = circ.getCircumference()
    radius = circ.getRadius()
    calc = 2. * math.pi * radius
    assert calc == cumfrence