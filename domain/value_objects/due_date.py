from datetime import date, timedelta
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DueDate:

    _value: date

    def __post_init__(self):

        if not isinstance(self._value, date):
            raise TypeError("Date is not valid date format")

    @classmethod
    def today(cls) -> "DueDate":
        return cls(date.today())
    
    @classmethod
    def tomorrow(cls) -> "DueDate":
        return cls(date.today() + timedelta(days=1))

    @classmethod
    def next_week(cls) -> "DueDate":
        return cls(date.today() + timedelta(weeks=1))
    
    @classmethod
    def next_month(cls) -> "DueDate":
        return cls(date.today() + timedelta(days=30))


    def __str__(self) -> str:
        return self._value.strftime("%Y-%m-%d")
    
    def __repr__(self) -> str:
        return f"DueDate('{self._value}')"