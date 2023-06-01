from typing import List

from src.domain.customer.Customer import Customer
from src.domain.customer.Customers import Customers
from src.domain.group.GroupType import GroupType
from src.domain.group.Groups import Groups


class ClassifiedCustomers:
    __classified_customers: {GroupType.NONE: List[Customer], GroupType.GENERAL: List[Customer]
        , GroupType.VIP: List[Customer], GroupType.VVIP: List[Customer]}
    _instance = None

    def __new__(cls, *args, **kwargs):
        if ClassifiedCustomers._instance is None:
            ClassifiedCustomers._instance = super().__new__(cls)
            return ClassifiedCustomers._instance

    def __init__(self):
        self.__classified_customers = {GroupType.NONE: list(), GroupType.GENERAL: list(),
                                            GroupType.VIP: list(), GroupType.VVIP: list()}

    @staticmethod
    def get_instance():
        if not ClassifiedCustomers._instance:
            ClassifiedCustomers._instance = ClassifiedCustomers()
            return ClassifiedCustomers._instance
        else:
            return ClassifiedCustomers._instance

    def clear(self):
        self.__classified_customers = {GroupType.NONE: list(), GroupType.GENERAL: list(),
                                            GroupType.VIP: list(), GroupType.VVIP: list()}

    def add_none_customer(self, customer: Customer):
        self.__classified_customers[GroupType.NONE].append(customer)

    def add_general_customer(self, customer: Customer):
        self.__classified_customers[GroupType.GENERAL].append(customer)

    def add_vip_customer(self, customer: Customer):
        self.__classified_customers[GroupType.VIP].append(customer)

    def add_vvip_customer(self, customer: Customer):
        self.__classified_customers[GroupType.VVIP].append(customer)

    def get_none_customers(self) -> List[Customer]:
        return self.__classified_customers[GroupType.NONE]

    def get_general_customers(self) -> List[Customer]:
        return self.__classified_customers[GroupType.GENERAL]

    def get_vip_customers(self) -> List[Customer]:
        return self.__classified_customers[GroupType.VIP]

    def get_vvip_customers(self) -> List[Customer]:
        return self.__classified_customers[GroupType.VVIP]

    def get_customers_by_group_type(self, group_type: GroupType) -> List[Customer]:
        return self.__classified_customers[group_type]

    def get_classified_list(self) -> {GroupType.NONE: List[Customer], GroupType.GENERAL: List[Customer]
        , GroupType.VIP: List[Customer], GroupType.VVIP: List[Customer]}:
        return self.__classified_customers

    def get_sorted_dict_by_customer_name_ascending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_name, reverse=False)
        return new_dict

    def get_sorted_dict_by_customer_name_descending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_name, reverse=True)
        return new_dict

    def get_sorted_dict_by_customer_spent_money_ascending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_spent_money, reverse=False)
        return new_dict

    def get_sorted_dict_by_customer_spent_money_descending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_spent_money, reverse=True)
        return new_dict

    def get_sorted_dict_by_customer_spent_hour_ascending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_spent_hour, reverse=False)
        return new_dict

    def get_sorted_dict_by_customer_spent_hour_descending(self):
        new_dict = self.__classified_customers.copy()
        for group_type in new_dict.keys():
            self.__classified_customers[group_type].sort(key=lambda customer: customer.customer_spent_hour, reverse=True)
        return new_dict
