from vector import Vector
import pytest


def test_create():
    Vector(1, 2)

def test_create_fail():
    with pytest.raises(TypeError):
        Vector(1)


def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v = v1 + v2
    assert v.x == 4 and v.y == 6


def test_add_zero():
    v1 = Vector(0, 0)
    v2 = Vector(3, 4)
    v = v1 + v2
    assert v == v2

