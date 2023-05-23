from typing import Set, List

from src.domain.group.Group import Group
from src.domain.group.GroupType import GroupType


class Groups:
    _instance = None
    __groups: List[Group]

    def __new__(cls, *args, **kwargs):
        if Groups._instance is None:
            Groups._instance = super().__new__(cls)
            return Groups._instance

    def __init__(self):
        self.__groups: List[Group] = [Group(GroupType.NONE, 0, 0), Group(GroupType.GENERAL, 0, 0), Group(GroupType.VIP, 0, 0), Group(GroupType.VVIP, 0, 0)]

    @staticmethod
    def get_instance():
        if not Groups._instance:
            Groups._instance = Groups()
            return Groups._instance
        else:
            return Groups._instance

    def get_groups(self) -> List[Group]:
        return self.__groups

    def get_group_by_group_type(self, group_type: GroupType) -> Group:
        for group in self.__groups:
            if group.group_type == group_type:
                return group
        return None

    def set_group_by_group_type(self, group_type: GroupType, group: Group):
        for i in range(len(self.__groups)):
            if self.__groups[i].group_type == group_type:
                self.__groups[i] = group
                break
        return None
