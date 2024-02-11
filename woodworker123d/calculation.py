"""
---toml
file-name = calculation.py
file-uuid = 558dfe7e-d54f-40b8-a0ae-1c98d14fd6e5
project-name = woodworker123d
project-uuid = project_uuid
authors = "felix@42sol.eu"
dates = "current_iso_date"
"""

# [Imports]
import logging                  #!md| [see docs](https://docs.python.org/3/library/logging.html)
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from math import *              #!md| [see docs](https://https://docs.python.org/3/library/math.html)
#----
from . import common

logging.basicConfig(level=DEBUG)

# [Types]

# [Constants]

g_min_angle_top = (-80.0 * pi ) / 180.0
g_max_angle_top = (+80.0 * pi ) / 180.0
g_min_length = 0.0
g_min_thickness = 0.1
g_max_thickness_coefficient = 10.0
# [Classes]

from math import degrees, radians

def convert_to_degree(angle_in_radians: float) -> float:
    """Converts an angle from radians to degrees.

    Args:
        angle_in_radians (float): Angle in radians.

    Returns:
        float: Angle in degrees.
    """
    # [convert_to_degree: Debug Log]
    logging.debug(f"Converting {angle_in_radians=} to degrees.")

    angle_in_degrees = degrees(angle_in_radians)

    return angle_in_degrees


 
def convert_to_radians(angle_in_degrees: float) -> float:
    """Converts an angle from degrees to radians.

    Args:
        angle_in_degrees (float): Angle in degrees.

    Returns:
        float: Angle in radians.
    """
    # [convert_to_radians: Debug Log]
    logging.debug(f"Converting {angle_in_degrees=} to radians.")

    angle_in_radians = radians(angle_in_degrees)

    return angle_in_radians


def evaluate_length(value: float) -> bool:
    """evaluate if a length is valid

    Args:
        value (float): length to evaluate

    Returns:
        bool: True if the length is valid
    """
    if value <= g_min_length:
        raise ValueError(f"{value=} must be >= {g_min_length}")
    
    return True 


def evaluate_thickness(value: float, width: float, height: float) -> bool:
    """evaluate if a thickness is valid

    Args:
        value (float): length to evaluate

    Returns:
        bool: True if the length is valid
    """

    if value < g_min_thickness:
        raise ValueError(f"{value=} must be >= {g_min_thickness}")
    
    max_thickness = max(width,height) / g_max_thickness_coefficient
    if value > max_thickness:
        raise ValueError(f"{value=} must be <= {max_thickness} (depending on the {max(width,height)})")

    return True 

def calculate_top_length_with_angle( plank_length : float, angle : float, plank_thickness : float) -> float:
    """calculate how a planks length is if it is put in an angle.

    Args:
        plank_length (float): the length of the tilted plank
        angle (float): angle of tilt (g_min_angle_top) < angle < (g_max_angle_top)
        plank_thickness (float): the thickness of the plank ( g_min_thickness < thickness < plank_length / g_max_thickness_coefficient)

    Raises:
        ValueError: If the plank_length is too small
        ValueError: If the angle is too small or too big
        ValueError: If the thickness is out of range

    Returns:
        float: _description_
    """

    # [calculate_top_length_with_angle: Parameter Check]
    if plank_length <= g_min_length:
        raise ValueError(f"{plank_length=} must be >= {g_min_length}")
    if angle < g_min_angle_top:
        raise ValueError(f"{angle=} must be bigger than {g_min_angle_top}")
    if angle > g_max_angle_top:
        raise ValueError(f"{angle=} must be bigger than {g_max_angle_top}")
    if plank_thickness < g_min_thickness:
        raise ValueError(f"{plank_thickness=} must be >= {g_min_thickness}")
    max_thickness = plank_length / g_max_thickness_coefficient
    if plank_thickness > max_thickness:
        raise ValueError(f"{plank_thickness=} must be <= {max_thickness} (depending on the plank_length)")
    

    length_with_angle = plank_length * cos(angle)
    thickness_with_angle = plank_thickness * sin(angle)
    full_length = length_with_angle + thickness_with_angle
    logging.debug(f"calculate_top_length_with_angle: {plank_length=} {angle=} {plank_thickness=} -> {full_length=}")

    return full_length

# [Functions]



# [Execution]

# [End of File 995da215-4601-4502-afd9-woodworker123dfrom math import *             #!md| [see docs](https://)