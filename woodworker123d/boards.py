"""
file-name = plans.py
file-uuid = 55fdf3df-1f27-45d4-b551-995466ad89ac
project-name = woodwork123d
project-uuid = ff31d696-909f-4692-bfd8-8a1cd13344e3
authors = "felix@42sol.eu"
dates = "2024-02-11"
authors = "felix@42sol.eu"
dates = "2024-02-11"
"""

# [Imports]
from .common import UnitEnum

# [Types]

# [Classes]
# TODO: is Board a @Dataclass
class Board:
    """A board of wood
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

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self.name = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.width = value
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        self.height = value

    @property
    def depth(self):
        return self.depth
    
    @depth.setter
    def depth(self, value):
        self.depth = value

    @property
    def thickness(self):
        return self.thickness
    
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


    

# [Functions]

# [Execution]

# [End of File planks.py]