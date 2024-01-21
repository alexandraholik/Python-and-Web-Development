import pytest
import exercise4
import math

# A test to catch the exception thrown by the function check_points.
@pytest.mark.parametrize("side_a, side_b, side_c, perimeter, area", [
    (3, 4, 5, 12, 6),
    (1, 1, 1, 3, math.sqrt(1.5 * 0.5 ** 3))
])

def test_triangle(side_a, side_b, side_c, perimeter, area):
    triangle = exercise4.Triangle(side_a, side_b, side_c)
    assert triangle.perimeter == perimeter
    assert triangle.area == area

@pytest.mark.parametrize("side, perimeter, area", [
    (1, 4, 1),
    (2, 8, 4),
])

def test_square(side, perimeter, area):
    square = exercise4.Square(side)
    assert square.perimeter == perimeter
    assert square.area == area

@pytest.mark.parametrize("side_a, side_b, perimeter, area", [
    (1, 2, 6, 2),
    (2, 3, 10, 6),
])

def test_rectangle(side_a, side_b, perimeter, area):
    rectangle = exercise4.Rectangle(side_a, side_b)
    assert rectangle.perimeter == perimeter
    assert rectangle.area == area

@pytest.mark.parametrize("radius, perimeter, area", [
    (1, 2 * math.pi, math.pi),
    (2, 4 * math.pi, 4 * math.pi),
])

def test_circle(radius, perimeter,area):
    circle = exercise4.Circle(radius)
    assert circle.perimeter == perimeter
    assert circle.area == area

@pytest.mark.parametrize("radius, height, volume", [
    (1, 1, math.pi),
    (1, 2, 2 * math.pi),
])
def test_cylinder(radius, height, volume):
    cylinder = exercise4.Cylinder(radius, height)
    assert cylinder.cylinder_volume() == volume