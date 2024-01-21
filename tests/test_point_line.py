import pytest
import point_line
@pytest.mark.parametrize("x, y, expected", [
    (3, 4, 5),
    (0, 0, 0),
    (6, 8, 10)
])
def test_point_distance_from_origin(x, y, expected):
    point = point_line.Point(x, y)
    assert point.distance_from_origin() == expected

@pytest.mark.parametrize("start_x, start_y, end_x, end_y, expected_length", [
    (0, 0, 3, 4, 5),
    (1, 2, 1, 2, 0),
    (6, 8, 9, 12, 5)
])
def test_line_length(start_x, start_y, end_x, end_y, expected_length):
    start_point = point_line.Point(start_x, start_y)
    end_point = point_line.Point(end_x, end_y)
    line = point_line.Line(start_point, end_point)
    assert line.length() == expected_length
