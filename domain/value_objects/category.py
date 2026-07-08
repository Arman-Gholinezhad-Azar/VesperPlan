import re
from dataclasses import dataclass


_CATEGORY_PATTERN = re.compile(r"^[a-z0-9_\- ]+$")


@dataclass(frozen=True)
class Category:

    _value:str

    def __post_init__(self):

        if not isinstance(self._value, str):
            raise TypeError("Category should be string")

        formatted = self._value.strip().lower()
        length = len(formatted)

        if not formatted:
            raise ValueError("category cannot be empty!")

        if length > 15:
            raise ValueError("category cannot be more than 15 characters")
        
        if not re.search(_CATEGORY_PATTERN, formatted):
            raise ValueError("invalid category pattern. correct pattern: (work_house, work-house, work house, work ...)")
    
        object.__setattr__(self, "_value", formatted)

    def __str__(self) -> str:
        return self._value
    
    def __repr__(self) -> str:
        return str(self)