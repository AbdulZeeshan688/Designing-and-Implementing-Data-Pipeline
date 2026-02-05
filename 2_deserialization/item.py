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

    def display_price(self):
        print(f"Item: {self.name}, Cost: {self.value}")

