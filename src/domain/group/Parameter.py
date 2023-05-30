class Parameter:
    def __init__(self, spent_money: int , spent_hour: int):
        self.spent_money: int = spent_money
        self.spent_hour: int = spent_hour

    def __str__(self):
        return f"이용 금액: {self.spent_money}만원 이용 시간: {self.spent_hour}시간"

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        if isinstance(self, other):
            if self.spent_money == other.spent_money and self.spent_hour == other.spent_hour:
                return True

    def __hash__(self):
        return hash((self.spent_money, self.spent_hour))

    @staticmethod
    def of(spent_money: int, spent_hour: int):
        return Parameter(spent_money, spent_hour)

    @property
    def spent_money(self) -> int:
        return self.__spent_money

    @spent_money.setter
    def spent_money(self, spent_money: int):
        self.__spent_money = spent_money

    @property
    def spent_hour(self) -> int:
        return self.__spent_hour

    @spent_hour.setter
    def spent_hour(self, spent_hour: int):
        self.__spent_hour = spent_hour

