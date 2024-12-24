import pytest
import math
from geometric_lib.circle import area, perimeter


def test_area_circle():
    r = 10
    area_check = math.pi * 10 * 10

    res = area(r)

    assert res == area_check


def test_area_otric_radius_circle():
    r = -10

    with pytest.raises(ValueError):
        area(r)


def test_area_zero_radius_circle():
    r = 0

    with pytest.raises(ValueError):
        area(r)


def test_area_type_circle():
    r = "ten"

    with pytest.raises(TypeError):
        area(r)


def test_perimeter_circle():
    r = 10
    perimeter_check = 2 * math.pi * 10

    res = perimeter(r)

    assert res == perimeter_check


def test_perimeter_otric_radius_circle():
    r = -10

    with pytest.raises(ValueError):
        perimeter(r)


def test_perimeter_zero_radius_circle():
    r = 0

    with pytest.raises(ValueError):
        perimeter(r)


def test_perimeter_type_circle():
    r = "ten"

    with pytest.raises(TypeError):
        perimeter(r)
