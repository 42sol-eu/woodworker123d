"""
---toml
file-name = common.py
file-uuid = 0d4ae205-4bac-4a01-978c-0d172d5b71e7
project-name = woodwork123d
project-uuid = project_uuid
authors = "felix@42sol.eu"
dates = "current_iso_date"
"""

# [Imports]
from dataclasses import dataclass                   #!md|[see documentation](https://docs.python.org/3/library/dataclasses.html)
from enum import Enum                               #!md|[see documentation](https://docs.python.org/3/library/enum.html)

# [Types]
class UnitEnum(Enum):
    metric: str = "mm"
    imperial: str = "inch"


# [Classes]

# [Functions]

# [Execution]

# [End of File common]