from typing import Set, List

from src.domain.group.Group import Group
from src.domain.group.GroupType import GroupType
from src.domain.group.Parameter import Parameter


class Groups:
    _instance = None
    __groups: List[Group]

    def __new__(cls, *args, **kwargs):
        if Groups._instance is None:
            Groups._instance = super().__new__(cls)
            return Groups._instance

    def __init__(self):
        self.__groups: List[Group] = [Group(GroupType.NONE, Parameter.of(0, 0)), Group(GroupType.GENERAL, Parameter.of(0,0)), Group(GroupType.VIP, Parameter.of(0,0)), Group(GroupType.VVIP, Parameter.of(0,0))]

    @staticmethod
    def get_instance():
        if not Groups._instance:
            Groups._instance = Groups()
            return Groups._instance
        else:
            return Groups._instance

    def get_group_by_group_type(self, group_type: GroupType) -> Group:
        for group in self.__groups:
            if group.group_type == group_type:
                return group
        return None

    def get_all_groups(self) -> List[Group]:
        return self.__groups

    def set_group_by_group_type(self, group_type: GroupType, group: Group):
        for i in range(len(self.__groups)):
            if self.__groups[i].group_type == group_type:
                self.__groups[i] = group
                break
        return None

    def is_groups_initialized(self) -> bool:
        flag = True
        for group in self.__groups:
            if group.parameter.spent_hour == 0 and group.parameter.spent_money == 0 and group.group_type is not GroupType.NONE:
                flag = False
        return flag

    def get_group_lowest_type_not_initilized(self) -> Group:
        for group in self.__groups:
            if group.parameter.spent_hour == 0 and group.parameter.spent_money == 0 and group.group_type\
                    is not GroupType.NONE:
                return group
        return None

    def check_is_group_initialized_by_group_type(self, type: GroupType):
        group = self.get_group_by_group_type(type)
        if group.parameter.spent_hour == 0 and group.parameter.spent_money == 0:
            return False
        else:
            return True

    def set_group_parameter_by_group_type(self, group_type: GroupType, parameter: Parameter):
        for i in range(len(self.__groups)):
            if self.__groups[i].group_type == group_type:
                self.__groups[i].parameter = parameter
                break
