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
# TODO: rename project to woodwork123d
# TODO: include wood_plates.toml

# [Parameters]
P_wood_plates_file = "wood_plates.toml"
P_wood_material = "material.toml"

# [Classes]

class UnitEnum(Enum):
    metric: str = "mm"
    imperial: str = "inch"

@dataclass
class Plate:
    """Plate class
    """
    id: int
    name: str
    width: float
    height: float
    thickness: float
    unit: UnitEnum
    material: str

    def __str__(self):
        return f"- plate {self.id}: {self.name} of {self.material} {self.width} x {self.height} {self.unit}, thick={self.thickness} {self.unit} "

    def __repr__(self):
        return f"Plate {self.id=}: {self.name=}, {self.unit=}, {self.material=} {self.width=} x {self.height=} {self.unit}, {self.thickness=}"


    @property
    def material(self):
        return self.material

    @material.setter
    def material(self, value):
        self.material = value

    @name.setter
    def name(self, value):
        self.name = value

    @witdh.setter
    def width(self, value):
        self.width = value
    
    @height.setter
    def height(self, value):
        self.height = value

    @depth.setter
    def depth(self, value):
        self.depth = value

    @thickness.setter
    def thickness(self, value):
        self.thickness = value
    

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def volume(self):
        return self.area * self.thickness
    
    @property
    def weight(self):
        return self.volume * self.material.density

@dataclass
class Plates(list):


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

    def __init__(self, width: float, height: float, depth: float, thickness: float, material: str):
        self.width = width
        self.height = height
        self.depth = depth
        self.thickness = thickness
        self.material = material
        self.plates = plates

    def __str__(self):
        return f"Wooden birdhouse: {self.width} x {self.height} x {self.depth} mm, {self.thickness} mm thick,\n made of {self.material} with\nPlates:\n{len(self.plates)}"

    def __repr__(self):
        return f"Wooden birdhouse: {self.width} x {self.height} x {self.depth} mm, {self.thickness} mm thick, made of {self.material} with\nPlates:\n{len(self.plates)}"

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