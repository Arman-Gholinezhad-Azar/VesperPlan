from dataclasses import dataclass


@dataclass(frozen=True)
class TaskDiscription:

    _value:str

    def __post_init__(self):

        if not isinstance(self._value, str):
            raise TypeError("Task discription should be string!")
        
        formatted = self._value.strip()
        length = len(formatted)

        if length > 200:
            raise ValueError("Discripion is too long.")
        
        object.__setattr__(self, "_value", formatted)
    
    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return str(self)