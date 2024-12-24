import pytest
from geometric_lib.square import area, perimeter


def test_area_square():
    a = 10
    area_check = 100

    res = area(a)

    assert res == area_check


def test_area_otric_side_square():
    r = -10

    with pytest.raises(ValueError):
        area(r)


def test_area_zero_side_square():
    a = 0

    with pytest.raises(ValueError):
        area(a)


def test_area_type_square():
    r = "ten"

    with pytest.raises(TypeError):
        area(r)


def test_perimeter_square():
    a = 10
    perimeter_check = 40

    res = perimeter(a)

    assert res == perimeter_check


def test_perimeter_otric_side_square():
    a = -10

    with pytest.raises(ValueError):
        perimeter(a)


def test_perimeter_zero_side_square():
    a = 0

    with pytest.raises(ValueError):
        perimeter(a)


def test_perimeter_type_square():
    a = "ten"

    with pytest.raises(TypeError):
        perimeter(a)
