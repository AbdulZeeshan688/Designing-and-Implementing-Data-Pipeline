class CoinAcceptor:
    def __init__(self):
        # jab object banta hai tab constructor chalta hai
        # total coins ki tadaad
        self.__amount = 0
        # coins ki total value (euro)
        self.__value = 0.0

    def insertCoin(self, coin_value: float) -> None:
        # naya coin insert hone par
        self.__amount += 1
        self.__value += coin_value

    def getAmount(self) -> int:
        # total coins ki tadaad return karta hai
        return self.__amount

    def getValue(self) -> float:
        # total coins ki value return karta hai
        return self.__value

    def returnCoins(self) -> tuple[int, float]:
        # jitne coins aur unki value hai unko return kar rahe hain
        returned_amount = self.__amount
        returned_value = self.__value

        # coins wapas dene ke baad sab zero
        self.__amount = 0
        self.__value = 0.0

        return returned_amount, returned_value
