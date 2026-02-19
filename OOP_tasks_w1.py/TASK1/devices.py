from dataclasses import dataclass
from typing import ClassVar

@dataclass
class IoTDevice:
    # CSV ke liye separator define kiya
    SEPARATOR: ClassVar[str] = ','

    device_id: str
    location: str
    data_value: float
    device_type: str 

    @staticmethod
    def deserialize(row: str) -> 'IoTDevice':
        # Row ko split karke columns nikal rahe hain
        columns = row.strip().split(IoTDevice.SEPARATOR)
        return IoTDevice(
            device_id=columns[0],
            location=columns[1],
            data_value=float(columns[2]),
            device_type=columns[3]
        )

    def serialize(self) -> str:
        # Object ko wapis CSV string mein convert karne ke liye
        return f"{self.device_id}{IoTDevice.SEPARATOR}{self.location}{IoTDevice.SEPARATOR}{self.data_value}{IoTDevice.SEPARATOR}{self.device_type}"

    def display_info(self):
        # Device ki details screen par dikhane ke liye
        print(f"[{self.device_type}] ID: {self.device_id} | Location: {self.location} | Value: {self.data_value}")

# Inheritance ka istemal karte hue specific sensors banaye
class TemperatureSensor(IoTDevice):
    pass

class HumiditySensor(IoTDevice):
    pass

class MotionSensor(IoTDevice):
    pass