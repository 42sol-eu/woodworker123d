
# [Imports]
from dataclasses import dataclass
#----
from .common import UnitEnum, get_base_unit

# [Classes]
# Q: how to add a dict in a dataclass?
# A: add a dict as a parameter


@dataclass
class Material:
    id: int = 0
    name: str = ""
    count: int = 0
    unit: UnitEnum = get_base_unit()

    # Class variable to keep track of the next available ID
    _next_id = 1

    def __init__(self, name : str, count : int = 1, unit : UnitEnum = get_base_unit()):
        self.id = Material.generate_id()
        self.name = name
        self.count = count
        self.unit = unit

    @classmethod
    def generate_id(cls) -> int:
        """
        Generate a new ID starting from 1.
        """
        new_id = cls._next_id
        cls._next_id += 1
        return new_id
# TODO: add a class Material -> Base Class for Boards




# TODO: is plank-list a good idea or do we need a PartsList?
class MaterialsList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return f"Materials: {len(self)} - {len(self)} items."

    def __repr__(self):
        output = f"Materials: {len(self)}"
        for item in self:
            output += f"\n{item.__repr__}"
    
        return output
    
    def __append__(self, item):
        if isinstance(item, Material):
            super().append(item)
        else:
            raise ValueError(f"Item {item} is not a Material")