from typing import Final

from src.domain.group.Group import Group
from src.domain.group.GroupType import GroupType
from src.domain.group.Parameter import Parameter


class Customer:
    num_customers = 0

    def __init__(self, customer_id: str, customer_name: str, customer_spent_hour: int, customer_spent_money: int):
        Customer.num_customers += 1
        self.__customer_serial_id: Final[int] = Customer.num_customers
        self.__customer_name: str = customer_name
        self.__customer_id: str = customer_id
        self.__customer_spent_hour: int = customer_spent_hour
        self.__customer_spent_money: int = customer_spent_money
        self.__group: Group = Group.of(GroupType.NONE, Parameter.of(0,0))

    def __str__(self):
        return f"고객 고유 번호: {self.__customer_serial_id} 고객 아이디: {self.__customer_id} 고객 이름: {self.__customer_name} 이용 금액: {self.__customer_spent_money}만원 이용 시간: {self.__customer_spent_hour}시간"

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.__customer_serial_id == other.__customer_serial_id
        return False

    def __hash__(self):
        return hash(self.__customer_serial_id)

    @staticmethod
    def of(customer_id: str, customer_name: str, customer_spent_money: int, customer_spent_hour: int):
        return Customer(customer_id, customer_name, customer_spent_money, customer_spent_hour)

    @property
    def customer_serial_id(self) -> int:
        return self.__customer_serial_id

    @property
    def group(self) -> Group:
        return self.__group

    @group.setter
    def group(self, group: Group):
        self.__group = group

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        self.__customer_id = customer_id

    @property
    def customer_spent_hour(self):
        return self.__customer_spent_hour

    @customer_spent_hour.setter
    def customer_spent_hour(self, customer_spent_hour: int):
        self.__customer_spent_hour = customer_spent_hour

    @property
    def customer_spent_money(self):
        return self.__customer_spent_money

    @customer_spent_money.setter
    def customer_spent_money(self, customer_spent_money: int):
        self.__customer_spent_money = customer_spent_money
