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
import logging                  #!md| [see docs](https://docs.python.org/3/library/logging.html)
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=DEBUG)

#---
from .common import UnitEnum, get_base_unit
from .calculation import evaluate_length, evaluate_thickness 
from .material import Material


# [Types]

# [Classes]
# TODO: is Board a @Dataclass
class Board(Material):
    """A board of wood
    """
    _default_material : str = "beech" 
    _default_thickness : float = 10.0

    _width: float
    _height: float
    _thickness: float
    _material: str

    def __init__(self, name: str, width: float, height: float, thickness: float = None, material: str = None, unit: UnitEnum = get_base_unit()):
        
        if thickness is None:
            thickness = Board._default_thickness
        
        evaluate_length(width)
        evaluate_length(height)
        evaluate_thickness(thickness, width, height)
        
        super().__init__(name, count=1, unit=unit)
        self.width = width
        self.height = height
        self.thickness = thickness
        if material is None:
            self.material = Board._default_material


    def __str__(self):
        return f"- plate {self.id}: {self.name} of {self.material} {self.width} x {self.height} {self.unit}, thick={self.thickness} {self.unit} "

    def __repr__(self):
        return f"Plate {self.id=}: {self.name=}, {self.unit=}, {self.material=} {self.width=} x {self.height=} {self.unit}, {self.thickness=}"


    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        evaluate_length(value)
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        evaluate_length(value)
        self._height = value


    @property
    def thickness(self):
        return self._thickness
    
    @thickness.setter
    def thickness(self, value):
        evaluate_thickness(value, self._width, self._height)
        self._thickness = value
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def volume(self):
        return self.area * self.thickness
    
    @property
    def weight(self):
        return self.volume * self.material.density


    @classmethod
    def set_default_material(cls, value) :
        """
        Generate a new ID starting from 1.
        """
        cls._default_material = value

    @classmethod
    def set_default_thickness(cls, value) :
        """
        Generate a new ID starting from 1.
        """
        cls._default_thickness = value

    @classmethod
    def get_default_material(cls) -> str:
        """
        Generate a new ID starting from 1.
        """
        return cls._default_material

    @classmethod
    def get_default_thickness(cls) -> float:
        """
        Generate a new ID starting from 1.
        """
        return cls._default_thickness

# [Functions]

# [Execution]

# [End of File planks.py]