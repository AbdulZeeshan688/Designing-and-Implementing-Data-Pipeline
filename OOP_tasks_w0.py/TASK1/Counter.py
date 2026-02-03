class Counter:
    def __init__(self):
        # constructor chal raha hai jab object banega
        # count ko shuru mein 0 set kar rahe hain
        self.__count = 0

    def addCount(self) -> None:
        # count ki value mein 1 add kar rahe hain
        self.__count += 1

    def getCount(self) -> int:
        # current count ki value wapas return kar rahe hain
        return self.__count

    def zeroCount(self) -> None:
        # count ki value dobara 0 set kar rahe hain
        self.__count = 0
