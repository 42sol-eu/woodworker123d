import pytest
from math import pi, cos, sin

from woodworker123d import calculate_top_length_with_angle, convert_to_degree, convert_to_radians

def test_calculate_top_length_with_angle():
    plank_length = 10.0
    angle = pi / 4  # 45 degrees
    plank_thickness = 1.0

    expected_length = plank_length * cos(angle) + plank_thickness * sin(angle)
    calculated_length = calculate_top_length_with_angle(plank_length, angle, plank_thickness)
    assert calculated_length == pytest.approx(expected_length)

def test_calculate_top_length_with_angle_invalid_plank_length():
    plank_length = -1.0
    angle = pi / 4  # 45 degrees
    plank_thickness = 1.0

    with pytest.raises(ValueError):
        calculate_top_length_with_angle(plank_length, angle, plank_thickness)

def test_calculate_top_length_with_angle_invalid_angle():
    plank_length = 100.0
    angle = -pi  # Invalid angle
    plank_thickness = 1.0

    with pytest.raises(ValueError):
        calculate_top_length_with_angle(plank_length, angle, plank_thickness)

    angle = 2 * pi  # Invalid angle

    with pytest.raises(ValueError):
        calculate_top_length_with_angle(plank_length, angle, plank_thickness)

def test_calculate_top_length_with_angle_invalid_thickness():
    plank_length = 100.0
    angle = pi / 4  # 45 degrees
    plank_thickness = -1.0  # Invalid thickness

    with pytest.raises(ValueError):
        calculate_top_length_with_angle(plank_length, angle, plank_thickness)

    plank_thickness = 100.0  # Invalid thickness

    with pytest.raises(ValueError):
        calculate_top_length_with_angle(plank_length, angle, plank_thickness)

    plank_thickness = plank_length / 10.0  # Valid thickness

    # This shouldn't raise any errors
    calculate_top_length_with_angle(plank_length, angle, plank_thickness)


#---

def test_convert_to_degree():
    radians_angles = [0, pi / 4, pi / 2, 3 * pi / 4, pi]
    expected_degrees = [0, 45, 90, 135, 180]

    for rad_angle, expected_deg in zip(radians_angles, expected_degrees):
        assert convert_to_degree(rad_angle) == pytest.approx(expected_deg)


def test_convert_to_radians():
    degree_angles = [0, 45, 90, 135, 180]
    expected_radians = [0, pi / 4, pi / 2, 3 * pi / 4, pi]

    for deg_angle, expected_rad in zip(degree_angles, expected_radians):
        assert convert_to_radians(deg_angle) == pytest.approx(expected_rad)


def test_convert_to_degree_and_back():
    degrees = [0, 30, 45, 60, 90, 120, 180, 270, 360]
    
    for deg in degrees:
        assert convert_to_radians(convert_to_degree(deg)) == pytest.approx(deg)