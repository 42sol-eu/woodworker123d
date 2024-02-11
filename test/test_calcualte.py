import pytest
from math import pi, cos, sin

from woodworker123d import calculate_top_length_with_angle, convert_to_degree, convert_to_radians, evaluate_length, evaluate_thickness

# [angle calculation]

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


# [Convert]

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



# [evaluate]

# Constants used in the functions (replace with actual values)
from woodworker123d.calculation import g_min_length, g_min_thickness, g_max_thickness_coefficient


# Test cases for evaluate_length
@pytest.mark.parametrize("value", [
    0.1,  # Minimum valid value
    1,  # Value greater than minimum
    5.5,  # Arbitrary valid value
])
def test_evaluate_length_valid(value):
    assert evaluate_length(value) == True

@pytest.mark.parametrize("value", [
    -1,  # Negative value
    -5.5,  # Negative value
    g_min_length - 0.1,  # Value just below minimum
])
def test_evaluate_length_invalid(value):
    with pytest.raises(ValueError):
        evaluate_length(value)

# Test cases for evaluate_thickness
@pytest.mark.parametrize("value, width, height", [
    (1, 10, 2),  # Arbitrary valid value
    (0.5, 10, 1),  # Value less than maximum based on width and height
])
def test_evaluate_thickness_valid(value, width, height):
    assert evaluate_thickness(value, width, height) == True

@pytest.mark.parametrize("value, width, height", [
    (-1, 2, 2),  # Negative value
    (5, 2, 1),  # Value greater than maximum based on width and height
    (2, 1, 5),  # Value greater than maximum based on width and height
])
def test_evaluate_thickness_invalid(value, width, height):
    with pytest.raises(ValueError):
        evaluate_thickness(value, width, height)