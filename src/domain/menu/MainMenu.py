from src.domain.menu.GroupMenu import GroupMenu
from src.domain.menu.Menu import Menu
from src.domain.menu.SummaryMenu import SummaryMenu
from src.util.Validator import Validator


class MainMenu(Menu):
    _instance = None
    __customer_menu: Menu
    __group_menu: Menu
    __summary_menu = Menu

    def __new__(cls, *args, **kwargs):
        if MainMenu._instance is None:
            MainMenu._instance = super().__new__(cls)
            return MainMenu._instance

    def __init__(self, customer_menu: Menu, group_menu: Menu, summary_menu: Menu):
        self.__customer_menu = customer_menu
        self.__group_menu = group_menu
        self.__summary_menu = summary_menu

    @staticmethod
    def get_instance():
        if MainMenu._instance is None:
            from src.domain.menu.CustomerMenu import CustomerMenu
            MainMenu._instance = MainMenu(CustomerMenu.get_instance(), GroupMenu.get_instance(),SummaryMenu.get_instance())
            return MainMenu._instance
        else:
            return MainMenu._instance

    def print_menu(self):
        print("메인 메뉴")
        print("1. 고객 관리")
        print("2. 그룹 관리")
        print("3. 요약 메뉴")
        print("0. 종료")
        menu_input = self.get_input()
        self.select_menu(menu_input)

    def select_menu(self, menu_input: int):
        if menu_input == 1:
            self.__customer_menu.print_menu()
        elif menu_input == 2:
            self.__group_menu.print_menu()
        elif menu_input == 3:
            self.__summary_menu.print_menu()
