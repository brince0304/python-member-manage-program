from typing import List
from typing import Set

from src.domain.customer.Customer import Customer


class Customers:
    _instance = None
    __customers: List[Customer]

    def __new__(cls, *args, **kwargs):
        if Customers._instance is None:
            Customers._instance = super().__new__(cls)
            return Customers._instance

    def __init__(self):
        self.__customers: List[Customer] = list()

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)

    def get_customer_by_customer_serial_id(self, customer_serial_id: int) -> Customer:
        for customer in self.__customers:
            if customer.customer_serial_id == customer_serial_id:
                return customer
        return None

    def delete_customer_by_customer_serial_id(self, customer_serial_id: int) -> bool:
        for customer in self.__customers:
            if customer.customer_serial_id == customer_serial_id:
                self.__customers.remove(customer)
                return True

    def is_exist_by_customer_serial_id(self, customer_serial_id: int) -> bool:
        for customer in self.__customers:
            if customer.customer_serial_id == customer_serial_id:
                return True
        return False

    def is_exist_by_customer_id(self, customer_id: str) -> bool:
        for customer in self.__customers:
            if customer.customer_id == customer_id:
                return True
        return False

    def edit_customer_by_customer_serial_id(self, customer_serial_id: int, customer: Customer) -> bool:
        for i in range(len(self.__customers)):
            if self.__customers[i].customer_serial_id == customer_serial_id:
                self.__customers[i] = customer
                return True
        return False

    def get_size(self) -> int:
        return len(self.__customers)

    def get_customer_by_index(self, index: int) -> Customer:
        return self.__customers[index]

    @staticmethod
    def get_instance():
        if not Customers._instance:
            Customers._instance = Customers()
            return Customers._instance
        else:
            return Customers._instance
