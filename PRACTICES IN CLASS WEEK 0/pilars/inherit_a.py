class Animal:
    sound: str

    def __init__(self, sound: str) -> None:
        self.sound = sound
        return None

    def makeSound(self) -> None:
        print(self.sound)
        return None


class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("Meow!")
        return None


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("Wuff!")
        return None


