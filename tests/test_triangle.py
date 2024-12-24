import pytest
from geometric_lib.triangle import area, perimeter


def test_area_triangle():
    a, b, c = 3, 4, 5
    area_check = 6

    res = area(a, b, c)

    assert res == area_check


def test_area_otric_side_triangle():
    a, b, c = -3, 4, 5

    with pytest.raises(ValueError):
        area(a, b, c)


def test_area_zero_side_triangle():
    a, b, c = 0, 4, 5

    with pytest.raises(ValueError):
        area(a, b, c)


def test_area_invalid_sides_triangle():
    a, b, c = 1, 2, 5

    with pytest.raises(ValueError):
        area(a, b, c)


def test_area_type_triangle():
    a, b, c = "three", 4, 5

    with pytest.raises(TypeError):
        area(a, b, c)


def test_perimeter_triangle():
    a, b, c = 3, 4, 5
    perimeter_check = 12

    res = perimeter(a, b, c)

    assert res == perimeter_check


def test_perimeter_otric_side_triangle():
    a, b, c = -3, 4, 5

    with pytest.raises(ValueError):
        perimeter(a, b, c)


def test_perimeter_zero_side_triangle():
    a, b, c = 0, 4, 5

    with pytest.raises(ValueError):
        perimeter(a, b, c)


def test_perimeter_invalid_sides_triangle():
    a, b, c = 1, 2, 5

    with pytest.raises(ValueError):
        perimeter(a, b, c)


def test_perimeter_type_triangle():
    a, b, c = "three", 4, 5

    with pytest.raises(TypeError):
        perimeter(a, b, c)
