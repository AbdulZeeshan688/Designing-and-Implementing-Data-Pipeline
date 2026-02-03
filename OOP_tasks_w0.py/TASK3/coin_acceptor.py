class CoinAcceptor:
    def __init__(self):
        # constructor jab object banta hai tab chalta hai
        # amount coins ki total tadaad rakhega
        self.__amount = 0
        # value future use ke liye hai (abhi use nahi ho rahi)
        self.__value = 0.0

    def insertCoin(self) -> None:
        # jab coin insert hota hai to amount mein 1 add hota hai
        self.__amount += 1

    def getAmount(self) -> int:
        # total coins ki tadaad wapas return kar rahe hain
        return self.__amount

    def returnCoins(self) -> int:
        # jitne coins hain unko return kar rahe hain
        returned = self.__amount
        # coins wapas karne ke baad amount zero kar dete hain
        self.__amount = 0
        return returned
