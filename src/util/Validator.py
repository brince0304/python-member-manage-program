import re


class Validator:
    regex_customer_name = re.compile("^[a-zA-Z]{3,}$")
    regex_customer_id = re.compile("^[a-zA-Z]{3,}$")
    customer_name_not_valid = "고객 이름이 유효하지 않습니다."
    customer_id_not_valid = "고객 아이디가 유효하지 않습니다."
    go_back_menu = "이전 메뉴로 돌아갑니다."
    yes_or_no_not_valid = "y 혹은 n만 입력해주세요."
    customer_id_already_exist = "이미 존재하는 고객 아이디입니다."

    @staticmethod
    def validate_customer_id(customer_id):
        if Validator.regex_customer_id.match(customer_id) is None:
            return False
        else:
            return True

    @staticmethod
    def validate_customer_name(customer_name):
        if Validator.regex_customer_name.match(customer_name) is None:
            return False
        else:
            return True

    @staticmethod
    def validate_is_go_back_menu(input_menu):
        if input_menu == "0":
            print(Validator.go_back_menu)
            return True
        else:
            return False

    @staticmethod
    def validate_is_yes_or_no(input_menu):
        ignore_case = input_menu.lower()
        if ignore_case == "y" or ignore_case == "n":
            return True
        else:
            return False
