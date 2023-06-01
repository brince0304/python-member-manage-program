from src.domain.customer.ClassifiedCustomers import ClassifiedCustomers
from src.domain.customer.Customers import Customers
from src.domain.group.GroupType import GroupType
from src.domain.group.Groups import Groups
from src.domain.menu.Menu import Menu
from src.util.MenuUtility import MenuUtility
from src.util.Validator import Validator


class SummaryMenu(Menu):
    _instance = None
    __classified_customer_service: ClassifiedCustomers
    __group_service: Groups
    __customer_service: Customers

    def __new__(cls, *args, **kwargs):
        if SummaryMenu._instance is None:
            SummaryMenu._instance = super().__new__(cls)
            return SummaryMenu._instance

    def __init__(self, classified_customer_service: ClassifiedCustomers, group_service: Groups, customer_service: Customers):
        self.__classified_customer_service = classified_customer_service
        self.__group_service = group_service
        self.__customer_service = customer_service

    @staticmethod
    def get_instance():
        if SummaryMenu._instance is None:
            SummaryMenu._instance = SummaryMenu(ClassifiedCustomers.get_instance(), Groups.get_instance(), Customers.get_instance())
            return SummaryMenu._instance
        else:
            return SummaryMenu._instance

    def print_menu(self):
        if self.__customer_service.get_size() == 0 or self.__group_service.is_groups_initialized() is False:
            print("고객 명단 또는 그룹 명단이 초기화되지 않았습니다.")
            return
        self.classified_customers()
        mode = True
        while mode:
            print("그룹별 조회 메뉴입니다.")
            print("1. 엑셀 파일로 내보내기")
            print("2. 그룹별 고객 명단 조회")
            print("3. 뒤로가기")
            print("0. 종료")
            menu_input = self.get_input()
            if menu_input == 3:
                break
            self.select_menu(menu_input)

    def select_menu(self, menu_input: int):
        if menu_input == 1:
            self.export_excel_select()
        elif menu_input == 2:
            self.print_customers_by_group_select()

    def print_customers_by_group_select(self):
        print("그룹별 고객 명단을 조회합니다.")
        print("정렬 순서를 선택해주세요.")
        print("1. 정렬 없음")
        print("2. 고객명 오름차순")
        print("3. 고객명 내림차순")
        print("4. 고객별 구매금액 오름차순")
        print("5. 고객별 구매금액 내림차순")
        print("6. 고객별 구매시간 오름차순")
        print("7. 고객별 구매시간 내림차순")
        print("8. 뒤로가기")
        print("0. 종료")
        while True:
            try:
                menu_input = self.get_input()
                if menu_input == 8:
                    return
                self.print_customers_by_menu_input(menu_input)
                break
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

    def print_customers_by_menu_input(self,menu_input : int):
        if menu_input == 1:
            self.print_customers_by_group()
        elif menu_input == 2:
            self.print_customers_by_customer_name_asc()
        elif menu_input == 3:
            self.print_customers_by_customer_name_desc()
        elif menu_input == 4:
            self.print_customers_by_customer_spent_money_asc()
        elif menu_input == 5:
            self.print_customers_by_customer_spent_money_desc()
        elif menu_input == 6:
            self.print_customers_by_customer_spent_hours_asc()
        elif menu_input == 7:
            self.print_customers_by_customer_spent_hours_desc()
        else:
            return

    def export_excel_select(self):
        print("엑셀파일로 내보내기")
        print("전체 명단을 엑셀파일로 내보냅니다.")
        print("정렬 순서를 선택해주세요.")
        print("1. 정렬 없음")
        print("2. 고객명 오름차순")
        print("3. 고객명 내림차순")
        print("4. 고객별 구매금액 오름차순")
        print("5. 고객별 구매금액 내림차순")
        print("6. 고객별 구매시간 오름차순")
        print("7. 고객별 구매시간 내림차순")
        print("8. 뒤로가기")
        print("0. 종료")
        try:
            while True:
                menu_input = self.get_input()
                sorted_dict = self.get_dict_by_menu_input(menu_input)
                if sorted_dict is None:
                    return
                else:
                    break
        except ValueError:
            print("메뉴는 숫자로 입력해주세요.")
            return
        print("파일명을 입력해주세요.")
        file_name = input()
        print(f"파일은 현재 경로에 저장됩니다. 저장될 파일명 : {file_name}")
        print("저장하시겠습니까? (y/n)")
        while True:
            is_save = input()
            if Validator.validate_is_yes_or_no(is_save):
                if is_save == "y":
                    self.export_excel(file_name, sorted_dict)
                print("저장되었습니다.")
                break
            else:
                print("y 또는 n을 입력해주세요.")
                continue

    def get_dict_by_menu_input(self, menu_input) -> dict:
        if menu_input == 1:
            return self.__classified_customer_service.get_classified_list()
        elif menu_input == 2:
            return self.__classified_customer_service.get_sorted_dict_by_customer_name_ascending()
        elif menu_input == 3:
            return self.__classified_customer_service.get_sorted_dict_by_customer_name_descending()
        elif menu_input == 4:
            return self.__classified_customer_service.get_sorted_dict_by_customer_spent_money_ascending()
        elif menu_input == 5:
            return self.__classified_customer_service.get_sorted_dict_by_customer_spent_money_descending()
        elif menu_input == 6:
            return self.__classified_customer_service.get_sorted_dict_by_customer_spent_hour_ascending()
        elif menu_input == 7:
            return self.__classified_customer_service.get_sorted_dict_by_customer_spent_hour_descending()
        else:
            return None

    def print_customers_by_group(self):
        classified_customers = self.__classified_customer_service.get_classified_list()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_name_asc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_name_ascending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_name_desc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_name_descending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_spent_money_asc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_spent_money_ascending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_spent_money_desc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_spent_money_descending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_spent_hours_asc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_spent_hour_ascending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def print_customers_by_customer_spent_hours_desc(self):
        classified_customers = self.__classified_customer_service.get_sorted_dict_by_customer_spent_hour_descending()
        for key in classified_customers.keys():
            print(MenuUtility.get_group_type(key))
            for customer in classified_customers[key]:
                print(customer)

    def export_excel(self, file_name: str, sorted_dict: dict):
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "그룹별 분류"
        ws.append(["그룹", "고객 아이디", "고객 이름", "총 구매금액(만원)", "총 구매시간(시간)"])
        for key in sorted_dict.keys():
            for customer in sorted_dict[key]:
                key = MenuUtility.get_group_type(key)
                id = customer.customer_id
                name = customer.customer_name
                spent_money = customer.customer_spent_money
                spent_hour = customer.customer_spent_hour
                ws.append([key, id, name, spent_money, spent_hour])
        wb.save(file_name + ".xlsx")

    def classified_customers(self):
        customers = self.__customer_service.get_customers()
        self.__classified_customer_service.clear()
        for customer in customers:
            if customer.group.group_type == GroupType.NONE:
                self.__classified_customer_service.add_none_customer(customer)
            elif customer.group.group_type == GroupType.GENERAL:
                self.__classified_customer_service.add_general_customer(customer)
            elif customer.group.group_type == GroupType.VIP:
                self.__classified_customer_service.add_vip_customer(customer)
            elif customer.group.group_type == GroupType.VVIP:
                self.__classified_customer_service.add_vvip_customer(customer)
            else:
                continue
