import pytest
import math
from geometric_lib.calculate import calc


def test_calc_input_area_circle():
    fig = "circle"
    func = "area"
    size = [10]
    check = math.pi * 10 * 10

    res = calc(fig, func, size)

    assert res == check


def test_calc_input_perimeter_square():
    fig = "square"
    func = "perimeter"
    size = [10]
    check = 40

    res = calc(fig, func, size)

    assert res == check


def test_calc_invalid_figure():
    fig = "a"
    func = "area"
    size = [10]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_invalid_function():
    fig = "circle"
    func = "a"
    size = [10]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_size_area():
    fig = "circle"
    func = "area"
    size = [10, 10, 10]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_otric_radius_circle():
    fig = "circle"
    func = "area"
    size = [-10]

    with pytest.raises(ValueError):
        calc(fig, func, size)


def test_calc_size_square():
    fig = "square"
    func = "area"
    size = [10, 10, 10]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_otric_side_square():
    fig = "square"
    func = "area"
    size = [-10]

    with pytest.raises(ValueError):
        calc(fig, func, size)


def test_calc_type_size():
    fig = "circle"
    func = "area"
    size = ["ten"]

    with pytest.raises(TypeError):
        calc(fig, func, size)


def test_calc_empty_size():
    fig = "circle"
    func = "area"
    size = []

    with pytest.raises(AssertionError):
        calc(fig, func, size)
