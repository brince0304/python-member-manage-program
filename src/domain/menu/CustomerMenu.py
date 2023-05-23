from src.domain.customer.Customer import Customer
from src.domain.customer.Customers import Customers
from src.domain.menu.Menu import Menu
from src.util.Validator import Validator


class CustomerMenu(Menu):
    _instance = None
    __customer_service: Customers

    def __new__(cls, *args, **kwargs):
        if CustomerMenu._instance is None:
            CustomerMenu._instance = super().__new__(cls)
            return CustomerMenu._instance

    def __init__(self, customer_service: Customers):
        self.__customer_service = customer_service

    @staticmethod
    def get_instance():
        if CustomerMenu._instance is None:
            CustomerMenu._instance = CustomerMenu(Customers.get_instance())
            return CustomerMenu._instance
        else:
            return CustomerMenu._instance

    def print_menu(self):
        mode = True
        while mode:
            print("고객 관리 메뉴")
            print("1. 고객 추가")
            print("2. 고객 삭제")
            print("3. 고객 수정")
            print("4. 고객 조회")
            print("5. 돌아가기")
            print("0. 종료")
            menu_input = self.get_input()
            if menu_input == 5:
                mode = False
            self.select_menu(menu_input)

    def select_menu(self, menu_input: int):
        if menu_input == 1:
            self.add_customer()
        elif menu_input == 2:
            self.delete_customer()
        elif menu_input == 4:
            self.print_customers()

    def add_customer(self):
        print("고객 명단을 추가합니다.")
        print("추가를 원하는 인원 수를 입력해주세요. 돌아가기를 원할 시 0을 입력해주세요.")
        try:
            num = int(input())
            if Validator.validate_is_go_back_menu(num):
                return
        except ValueError:
            print("숫자만 입력해주세요. 돌아갑니다.")
            return
        self.add_customer_recall(num)

    def add_customer_recall(self, num: int):
        for i in range(num):
            print(f"{i + 1}번째 고객 정보를 입력하세요.")
            print("이전으로 돌아가기를 원할 시 0을 입력해주세요.")
            while True:
                customer_id = input("고객 ID를 입력해주세요. (알파벳 / 숫자 / _ 가능, 5~12자, 첫글자는 영문자 혹은 숫자, 중복 금지)")
                if Validator.validate_is_go_back_menu(customer_id):
                    return
                if self.__customer_service.is_exist_by_customer_id(customer_id):
                    print(Validator.customer_id_already_exist)
                elif Validator.validate_customer_id(customer_id):
                    break
                else:
                    print(Validator.customer_id_not_valid)
            while True:
                customer_name = input("고객 이름을 입력해주세요. (영문자, 3자 이상)")
                if Validator.validate_is_go_back_menu(customer_name):
                    return
                if Validator.validate_customer_name(customer_name):
                    break
                else:
                    print(Validator.customer_name_not_valid)
            while True:
                try:
                    customer_spent_money = int(input("고객 이용 금액을 만원 단위로 1이상 입력 해주세요. (숫자)"))
                    if Validator.validate_is_go_back_menu(customer_spent_money):
                        return
                    if customer_spent_money < 0:
                        print("0 이상의 숫자를 입력해주세요.")
                    else:
                        break
                except ValueError:
                    print("숫자만 입력해주세요.")
            while True:
                try:
                    customer_spent_hour = int(input("고객 이용 시간을 시간 단위로 1이상 입력 해주세요. (숫자)"))
                    if Validator.validate_is_go_back_menu(customer_spent_hour):
                        return
                    if customer_spent_hour < 0:
                        print("0 이상의 숫자를 입력해주세요.")
                    else:
                        break
                except ValueError:
                    print("숫자만 입력해주세요.")
            print(
                f"고객 ID: {customer_id}, 고객 이름: {customer_name}, 고객 이용 금액: {customer_spent_money}, 고객 이용 시간: {customer_spent_hour}")
            print("이 정보를 추가하시겠습니까? (y/n) 이전 메뉴로 돌아가시려면 0을 입력해주세요.")
            while True:
                reply = input()
                if Validator.validate_is_go_back_menu(reply):
                    return
                if Validator.validate_is_yes_or_no(reply):
                    break
                else:
                    print(Validator.yes_or_no_not_valid)
            if reply == 'y':
                self.__customer_service.add_customer(
                    Customer.of(customer_id, customer_name, customer_spent_money, customer_spent_hour))
                print(f"{i + 1}번째 고객 정보가 추가되었습니다.")
            else:
                print("고객 정보 추가를 취소합니다.")
        print("모든 고객 정보가 추가되었습니다.")

    def print_customers(self):
        if self.__customer_service.get_size() == 0:
            print("고객 명단이 비어있습니다.")
            return
        print("고객 명단을 출력합니다.")
        for i in range(self.__customer_service.get_size()):
            customer = self.__customer_service.get_customer_by_index(i)
            print(
                f"고유 번호 : {customer.customer_serial_id} 고객 ID: {customer.customer_id}, 고객 이름: {customer.customer_name}, 고객 이용 금액: {customer.customer_spent_money}, 고객 이용 시간: {customer.customer_spent_hour}")
        print("고객 명단 출력을 완료하였습니다.")

    def delete_customer(self):
        if self.__customer_service.get_size() == 0:
            print("고객 명단이 비어있습니다.")
            return
        print("고객 명단을 삭제합니다.")
        print("삭제를 원하는 인원 수를 입력해주세요. 돌아가기를 원할 시 0을 입력해주세요.")
        try:
            num = int(input())
            if Validator.validate_is_go_back_menu(num):
                return
        except ValueError:
            print("숫자만 입력해주세요. 돌아갑니다.")
            return
        self.delete_customer_recall(num)

    def delete_customer_recall(self, num):
        for i in range(num):
            print("삭제를 원하는 명단의 고유 번호를 입력해주세요. 돌아가기를 원할 시 0을 입력해주세요.")
            try:
                serial_id = int(input())
                if Validator.validate_is_go_back_menu(serial_id):
                    return
            except ValueError:
                print("숫자만 입력해주세요. 돌아갑니다.")
                return
            if self.__customer_service.is_exist_by_customer_serial_id(serial_id):
                self.__customer_service.delete_customer_by_customer_serial_id(serial_id)
                print(f"{serial_id}번째 고객 정보가 삭제되었습니다.")
            else:
                print("해당 고유 번호의 고객 정보가 존재하지 않습니다.")
        print("모든 고객 정보가 삭제되었습니다.")




