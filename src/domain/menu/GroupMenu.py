from src.domain.group.GroupType import GroupType
from src.domain.group.Groups import Groups
from src.domain.group.Parameter import Parameter
from src.domain.menu.Menu import Menu


class GroupMenu(Menu):
    _instance = None
    __group_service: Groups

    def __new__(cls, *args, **kwargs):
        if GroupMenu._instance is None:
            GroupMenu._instance = super().__new__(cls)
            return GroupMenu._instance

    def __init__(self, group_service: Groups):
        self.__group_service = group_service

    @staticmethod
    def get_instance():
        if GroupMenu._instance is None:
            GroupMenu._instance = GroupMenu(Groups.get_instance())
            return GroupMenu._instance
        else:
            return GroupMenu._instance

    def print_menu(self):
        mode = True
        while mode:
            print("그룹 관리")
            print("1. 그룹 기준 초기 설정")
            print("2. 그룹 기준 수정")
            print("3. 그룹 기준 조회")
            print("4. 돌아가기")
            print("0. 종료")
            menu_input = self.get_input()
            if menu_input == 4:
                mode = False
            self.select_menu(menu_input)

    def select_menu(self, menu_input: int):
        if menu_input == 1:
            self.init_group_parameter_select()
        elif menu_input == 2:
            self.update_group_parameter_select()
        if menu_input == 3:
            self.print_group_parameter()

    def init_group_parameter_select(self):
        if self.__group_service.is_groups_initialized():
            print("이미 그룹 기준이 초기화 되었습니다.")
            return
        else:
            self.init_group_parameter()

    def init_group_parameter(self):
        print("그룹 기준을 초기화합니다.")
        print("그룹은 4개로 나뉘어집니다.")
        print("1. NONE, 2. GENERAL, 3. VIP, 4. VVIP")
        print("GENERAL 그룹의 기준 이하는 NONE 으로 분류됩니다.")
        print("GENERAL 그룹부터 설정되지 않은 순서대로 기준을 설정합니다.")
        if self.__group_service.is_groups_initialized():
            print("모든 그룹 기준이 초기화되었습니다.")
            return
        else:
            self.init_group_parameter_from_lowest_type()

    def init_group_parameter_from_lowest_type(self):
        mode = True
        while mode is True:
            if self.__group_service.is_groups_initialized():
                print("모든 그룹 기준이 초기화되었습니다.")
                return
            group = self.__group_service.get_group_lowest_type_not_initilized()
            print(f"{group.group_type} 그룹 기준을 초기화합니다.")
            print("돌아가시려면 0을 입력해주세요. 0보다 적은 숫자를 입력시에도 종료됩니다.")
            while True:
                try:
                    spent_hour = int(input("시간 기준을 입력해주세요. (단위: 시간) : "))
                    if spent_hour < 1:
                        mode = False
                        break
                    spent_money = int(input("금액 기준을 입력해주세요. (단위: 원) : "))
                    if spent_money < 1:
                        mode = False
                        break
                    if self.check_available_group_parameter_for_initialize(group.group_type, spent_money, spent_hour):
                        group.parameter = Parameter(spent_money, spent_hour)
                        self.__group_service.set_group_parameter_by_group_type(group.group_type, group.parameter)
                        break
                    else:
                        print("입력한 기준이 다른 그룹의 기준과 충돌합니다.")
                        continue
                except ValueError:
                    print("숫자를 입력해주세요.")
                    continue

    def check_available_group_parameter_for_initialize(self, group_type: GroupType, standard_spent_money: int,
                                                       standard_spent_hour: int):
        general_group = self.__group_service.get_group_by_group_type(GroupType.GENERAL)
        general_money_parameter = general_group.parameter.spent_money
        general_hour_parameter = general_group.parameter.spent_hour
        vip_group = self.__group_service.get_group_by_group_type(GroupType.VIP)
        vip_money_parameter = vip_group.parameter.spent_money
        vip_hour_parameter = vip_group.parameter.spent_hour
        vvip_group = self.__group_service.get_group_by_group_type(GroupType.VVIP)
        if group_type == GroupType.GENERAL:
            return True
        elif group_type == GroupType.VIP:
            if standard_spent_money <= general_money_parameter or standard_spent_hour <= general_hour_parameter:
                return False
            else:
                return True
        elif group_type == GroupType.VVIP:
            if standard_spent_money <= vip_money_parameter or standard_spent_hour <= vip_hour_parameter:
                return False
            else:
                return True

    def check_available_group_parameter(self, group_type: GroupType, standard_spent_money: int,
                                        standard_spent_hour: int):
        general_group = self.__group_service.get_group_by_group_type(GroupType.GENERAL)
        general_money_parameter = general_group.parameter.spent_money
        general_hour_parameter = general_group.parameter.spent_hour
        vip_group = self.__group_service.get_group_by_group_type(GroupType.VIP)
        vip_money_parameter = vip_group.parameter.spent_money
        vip_hour_parameter = vip_group.parameter.spent_hour
        vvip_group = self.__group_service.get_group_by_group_type(GroupType.VVIP)
        vvip_money_parameter = vvip_group.parameter.spent_money
        vvip_hour_parameter = vvip_group.parameter.spent_hour
        if group_type == GroupType.GENERAL:
            if standard_spent_money >= vip_money_parameter or standard_spent_hour >= vip_hour_parameter:
                return False
            else:
                return True
        elif group_type == GroupType.VIP:
            if standard_spent_money <= general_money_parameter or standard_spent_hour <= general_hour_parameter \
                    or standard_spent_money >= vvip_money_parameter or standard_spent_hour >= vvip_hour_parameter:
                return False
            else:
                return True
        elif group_type == GroupType.VVIP:
            if standard_spent_money <= vip_money_parameter or standard_spent_hour <= vip_hour_parameter or \
                    standard_spent_money <= general_money_parameter or standard_spent_hour <= general_hour_parameter:
                return False
            else:
                return True
        else:
            return False

    def print_group_parameter(self):
        if self.__group_service.is_groups_initialized() is False:
            print("그룹 기준이 초기화되지 않았습니다.")
            return
        for group in self.__group_service.get_all_groups():
            print(group)

    def get_group_name(self, group_type: GroupType):
        if group_type == GroupType.NONE:
            return "NONE"
        elif group_type == GroupType.GENERAL:
            return "GENERAL"
        elif group_type == GroupType.VIP:
            return "VIP"
        elif group_type == GroupType.VVIP:
            return "VVIP"
        else:
            return "NONE"

    def update_group_parameter_select(self):
        if self.__group_service.is_groups_initialized() is False:
            print("그룹 기준이 초기화되지 않았습니다.")
            return
        print("그룹 기준을 수정합니다.")
        print("1. GENERAL, 2. VIP, 3. VVIP")
        while True:
            try:
                group_type = int(input("수정할 그룹을 선택해주세요. : "))
                if group_type < 1 or group_type > 3:
                    print("1, 2, 3 중 하나를 입력해주세요.")
                    continue
                else:
                    if group_type == 1:
                        group_type = GroupType.GENERAL
                    elif group_type == 2:
                        group_type = GroupType.VIP
                    elif group_type == 3:
                        group_type = GroupType.VVIP
                    self.update_group_parameter(group_type)
                    print("그룹 기준이 수정되었습니다.")
                    break
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

    def update_group_parameter(self, group_type: GroupType):
        group = self.__group_service.get_group_by_group_type(group_type)
        print(f"{group.group_type} 그룹 기준을 수정합니다.")
        print("돌아가시려면 0을 입력해주세요. 0보다 적은 숫자를 입력시에도 종료됩니다.")
        while True:
            try:
                spent_hour = int(input("시간 기준을 입력해주세요. (단위: 시간) : "))
                if spent_hour < 1:
                    return
                spent_money = int(input("금액 기준을 입력해주세요. (단위: 원) : "))
                if spent_money < 1:
                    return
                if self.check_available_group_parameter(group_type, spent_money, spent_hour):
                    group.parameter = Parameter(spent_money, spent_hour)
                    self.__group_service.set_group_parameter_by_group_type(group_type, group.parameter)
                    break
                else:
                    print("입력한 기준이 다른 그룹의 기준과 충돌합니다.")
                    continue
            except ValueError:
                print("숫자를 입력해주세요.")
                continue
