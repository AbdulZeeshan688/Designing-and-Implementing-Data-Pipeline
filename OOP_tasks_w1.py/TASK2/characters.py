from abc import ABC, abstractmethod # ABSTRACT BASE CLASS .# YA ALLOW KARTA HA KA AISA DIRECTLY KOI USE NA KAR 
from dataclasses import dataclass
from typing import ClassVar
#“Any child class MUST write this function, or Python will give error.”"ABSTRACT CLASS

# Abstract Base Class definition
@dataclass
class GameCharacter(ABC):
    # ClassVar use kar rahe hain patterns follow karne ke liye
    TYPE_LABEL: ClassVar[str] = "Generic"

    name: str
    health: int = 100

    @abstractmethod
    def attack(self):
        # Yeh method har subclass mein implement hona zaroori hai
        pass

    @abstractmethod
    def defend(self):
        # Yeh method har subclass mein implement hona zaroori hai
        pass

# Warrior subclass implementation # INHERIT KAR RAHA GAME CHARACTER SA 
class Warrior(GameCharacter):
    TYPE_LABEL: ClassVar[str] = "Warrior"# WARRIOR KA TYPE LABEL CHANGE HO GIA GENERIC SA 

    def attack(self):
        print(f"{self.name} swings a heavy sword! (Damage: 20)")

    def defend(self):
        print(f"{self.name} blocks with a steel shield!")

# Mage subclass implementation
class Mage(GameCharacter):
    TYPE_LABEL: ClassVar[str] = "Mage"

    def attack(self):
        print(f"{self.name} casts a Fireball spell! (Damage: 25)")

    def defend(self):
        print(f"{self.name} creates a magical energy barrier!")

# Archer subclass implementation
class Archer(GameCharacter):
    TYPE_LABEL: ClassVar[str] = "Archer"

    def attack(self):
        print(f"{self.name} shoots a precise arrow! (Damage: 18)")

    def defend(self):
        print(f"{self.name} dodges the attack swiftly!")