"""
file-name: wooden_birdhouse.py
file-uuid: b92d4a7e-924c-420d-90b2-84a2aef558d0
project-name: woodwork123d
project-uuid: ff31d696-909f-4692-bfd8-8a1cd13344e3
authors: "felix@42sol.eu"
dates: "2024-02-11"
"""
# [Imports]
import toml                                         #!md|[see documentation](https://
from pathlib import Path                            #!md|[see documentation](https://docs.python.org/3/library/pathlib.html)
from dataclasses import dataclass                   #!md|[see documentation](https://docs.python.org/3/library/dataclasses.html)
from enum import Enum                               #!md|[see documentation](https://docs.python.org/3/library/enum.html)
#---
import common
from planks import Plank, PlanksList

# [Parameters]
P_wood_plates_file = "wood_plates.toml"
P_wood_material = "material.toml"

# [Types]

# [Classes]




@dataclass
class Birdhouse:
    """Birdhouse class
    """
    width: float
    height: float
    depth: float
    thickness: float
    material: str
    plates: list

    def __init__(self, 
                 width: float, 
                 height: float, 
                 depth: float, 
                 thickness: float, 
                 material: str, 
                 unit : common.UnitEnum = common.UnitEnum.metric  ):
        self.width = width
        self.height = height
        self.depth = depth
        self.thickness = thickness
        self.material = material
        self.unit = unit 
        self.plates = []

    def __str__(self):
        return f"Wooden birdhouse: {self.width} x {self.height} x {self.depth} mm, {self.thickness} mm thick,\n made of {self.material} with\nPlates:\n{len(self.plates)}"

    def __repr__(self):
        return f"Wooden birdhouse: {self.width} x {self.height} x {self.depth} mm, {self.thickness} mm thick, made of {self.material} with\nPlates:\n{len(self.plates)}"

    def add_plate(self, name, width, height, thickness = 0.0, material=""):
        """Add a plate to the birdhouse

        Args:
            name (str): name of the plate
            width (float): width of the plate
            height (float): height of the plate
            thickness (float): thickness of the plate
            material (str): material of the plate
        """
        if name in self.plate_names:
            raise ValueError(f"Plate {name} already exists")

        self.plate_names.append(name)

        if material == "":
            material = self.material
        if thickness == 0:
            thickness = self.thickness
        the_plank = Plank(name, width, height, thickness, material, unit=self.unit)
        self.plates.append(the_plank)

# [Functions]

# TODO: check if we better add variables for the file names
def load_data( path =  ".": str) -> (dict, dict):
    """load the data from the configuration files (toml format)

    Args:
        path (String, optional): The path to the configuration files. Defaults to "."

    Returns:
        materials (Dictionary): List of wooden materials
        plates (Dictionary): List of wooden plates
    """

    #!md| 1. load data from configuration  files

    with open(P_wood_material) as f:
        wood_material = toml.load(f)

    with open(P_wood_plates_file) as f:
        wood_plates = toml.load(f)

    return (wood_material, wood_plates)

def set_sizes(width: float, height: float, depth : float, thickness: float) -> dict:

# [Execution]

def main():
    """Main function
    """
    wood_material, wood_plates = load_data()
    print(wood_material)
    print(wood_plates)    

# [End of file: wooden_birdhouse.py]