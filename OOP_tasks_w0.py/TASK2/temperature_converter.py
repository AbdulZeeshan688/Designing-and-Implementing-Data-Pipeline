class TemperatureConverter:
    def __init__(self):
        # constructor jab object banta hai tab chalta hai
        # temperature ko shuru mein 0.0 set kar rahe hain
        self.__temperature = 0.0

    def setTemperature(self, temp: float) -> None:
        # user jo temperature de, usko set kar rahe hain
        self.__temperature = temp

    def toCelsius(self) -> float:
        # temperature already Celsius mein hai
        # isliye seedha wapas kar rahe hain
        return self.__temperature

    def toFahrenheit(self) -> float:
        # Celsius ko Fahrenheit mein convert kar rahe hain
        return (self.__temperature * 9 / 5) + 32

    def toKelvin(self) -> float:
        # Celsius ko Kelvin mein convert kar rahe hain
        return self.__temperature + 273.15
