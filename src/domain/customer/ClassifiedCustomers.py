from typing import List

from src.domain.customer.Customer import Customer


class ClassifiedCustomers:
    __classified_customers: List[Customer]
    _instance = None

    def __new__(cls, *args, **kwargs):
        if ClassifiedCustomers._instance is None:
            ClassifiedCustomers._instance = super().__new__(cls)
            return ClassifiedCustomers._instance

    def __init__(self):
        self.__classified_customers: List[Customer] = list()

    @staticmethod
    def get_instance():
        if not ClassifiedCustomers._instance:
            ClassifiedCustomers._instance = ClassifiedCustomers()
            return ClassifiedCustomers._instance
        else:
            return ClassifiedCustomers._instance
