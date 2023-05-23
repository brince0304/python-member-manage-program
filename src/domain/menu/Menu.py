import abc


class Menu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def print_menu(self):
        pass

    @abc.abstractmethod
    def select_menu(self, menu_input: int):
        pass

    def get_input(self):
        print("메뉴를 입력해주세요.")
        try:
            menu_input = int(input())
            if menu_input == 0:
                print("프로그램을 종료합니다.")
                quit()
        except ValueError:
            print("메뉴는 숫자로 입력해주세요.")
            return
        return menu_input
