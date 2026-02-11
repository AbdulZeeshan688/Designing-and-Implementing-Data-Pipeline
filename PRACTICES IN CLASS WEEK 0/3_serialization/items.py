from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Item:
    SEPARATOR: ClassVar[str] = ','

    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def deserialize(row: str) -> 'Item':
        columns = row.strip().split(Item.SEPARATOR)
        return Item(
            name=columns[0],
            value=float(columns[1]),
            category=columns[2],
            weight=float(columns[3])
        )

    # NEW: This function turns the object back into a CSV string
    def serialize(self) -> str:
        return f"{self.name}{Item.SEPARATOR}{self.value}{Item.SEPARATOR}{self.category}{Item.SEPARATOR}{self.weight}"

    # Updated to match the screenshot format (e.g., "Hat costs 20.0 €.")
    def display_info(self):
        print(f"{self.name} costs {self.value} €.")