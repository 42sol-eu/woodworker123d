
# [Imports]
from dataclasses import dataclass
#----
from .common import UnitEnum, get_base_unit

# [Classes]

@dataclass
class Material:
    id: str = ""
    name: str = ""
    count: int = 0
    data: dict = {}
    unit: UnitEnum = UnitEnum.metric

    def __init__(self, id : str, name : str, count : int = 1, data : dict = {}, unit : UnitEnum = get_base_unit()):
        self.id = id
        self.name = name
        self.count = count
        self.data = data
        self.unit = unit

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