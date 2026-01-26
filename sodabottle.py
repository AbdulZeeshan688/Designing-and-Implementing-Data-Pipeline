class SodaBottle:
    brand: str
    capopen: bool

    def __init__(self, brand) -> None:
        self.brand = brand
        self.capopen = False

    def openBottle(self) -> None:
        if not self.capopen:
            print("sihhh...")
            self.capopen = True

    def drink(self) -> None:
        if not self.capopen:
            print("Can't drink from a closed bottle...")
        else:
            print(f"Glunk glunk! mmm... tasts like {self.brand}")