"""
---toml
file-name = birdhouse_1.py
file-uuid = 324ddfa9-d670-4db7-a92c-b87ae5089470
project-name = woodwork123d
project-uuid = project_uuid
authors = "felix@42sol.eu"
dates = "current_iso_date"
"""

# [Imports]
import woodworker123d as ww
from math import sin, cos
# [Types]

# [Parameters]
p_thickness = 18

p_roof_depth = 230
p_roof_width = 200
p_height_difference = 40 # front to back
p_angle = sin( g_height_difference / g_depth)

# [Constants]
g_depth = g_roof_depth * cos(g_angle)
g_height = 
# [Functions]

# [Execution]
def main(name="a birdhouse"):
    print(f"Creating {name}")
    birdhouse = ww.Birdhouse(p_roof_width, g_height, g_depth, 10, "pine")
    print(birdhouse)
    print(f"Created {name} with {len(birdhouse.plates)} plates")
    print("Done.")


# [End of File birdhouse_1]