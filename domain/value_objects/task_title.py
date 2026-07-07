import re
from dataclasses import dataclass


_TASK_TITLE_PATTERN = re.compile(r"^[a-zA-Z0-9_.\- ]+$")

@dataclass(frozen=True)
class TaskTitle:

    _value: str

    def __post_init__(self):

        if not isinstance(self._value, str):
            raise TypeError("Task title should be string!")

        formatted = self._value.strip()
        length = len(formatted)

        if not formatted:
            raise ValueError("Task name should not be empty.")

        if length > 30:
            raise ValueError("Task name should not be more than 30 characters.")

        if not re.search(_TASK_TITLE_PATTERN, formatted):
            raise ValueError("Task name cannot use special characters like ($%^& etc). allowed special characters are: (_ . -)")

        object.__setattr__(self, "_value", formatted)

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return str(self)