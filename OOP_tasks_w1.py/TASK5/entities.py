# ==============================================================================
# Coder Name: Abdul Zeeshan Mirza
# Course: Designing and Implementing Data Pipelines
# Date: 2026-03-01
# Time: 12:01 EET
# Description: Virtual Reality Simulation Entities using Inheritance & Polymorphism
# ==============================================================================

from dataclasses import dataclass

@dataclass
class Entity:
    # Base class attributes jo har entity ke paas honge
    name: str
    position: str 

    def interact(self):
        # Base method jise subclasses apni marzi se override karengi
        pass

@dataclass
class Player(Entity):
    # Player ki specific property
    health: int = 100

    def interact(self):
        # Player ka interact karne ka apna tareeqa
        print(f"Player '{self.name}' at {self.position} is ready for action. Health: {self.health}HP.")

@dataclass
class NPC(Entity):
    # Non-Player Character ki specific property
    role: str = "Villager"

    def interact(self):
        # NPC ka interact karne ka apna tareeqa (Dialogue)
        print(f"NPC '{self.name}' at {self.position} says: 'Greetings! I am a {self.role}.'")

@dataclass
class Object(Entity):
    # Environment object ki specific property
    object_type: str = "Obstacle"

    def interact(self):
        # Object ka interact karne ka tareeqa (Bejaan cheez)
        print(f"Object '{self.name}' at {self.position} is a {self.object_type}. It does not respond.")