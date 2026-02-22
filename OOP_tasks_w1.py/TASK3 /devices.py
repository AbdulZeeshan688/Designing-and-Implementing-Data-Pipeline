from dataclasses import dataclass

@dataclass
class SmartDevice:
    device_name: str
    status: str = "OFF"

    def operate(self):
        # Base method
        pass

@dataclass
class SmartLight(SmartDevice):
    # Ab yeh attribute __init__ mein accept hoga
    brightness: int = 100

    def operate(self):
        self.status = "ON"
        print(f"SmartLight '{self.device_name}' is now {self.status} at {self.brightness}% brightness.")

@dataclass
class SmartThermostat(SmartDevice):
    # Dataclass decorator zaroori hai naye fields ke liye
    temperature: int = 22

    def operate(self):
        self.status = "ACTIVE"
        print(f"SmartThermostat '{self.device_name}' is {self.status}. Setting temp to {self.temperature}°C.")

@dataclass
class SmartLock(SmartDevice):
    def operate(self):
        self.status = "LOCKED"
        print(f"SmartLock '{self.device_name}' status updated to: {self.status}.")