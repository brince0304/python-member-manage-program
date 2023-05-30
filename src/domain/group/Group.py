from src.domain.group.GroupType import GroupType
from src.domain.group.Parameter import Parameter


class Group :
    def __init__(self, group_type: GroupType, parameter: Parameter):
        self.__group_type: GroupType = group_type
        self.__parameter: Parameter = parameter

    def __str__(self):
        return f"그룹 타입: {self.__group_type}, {self.__parameter}"

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        if isinstance(self, other):
            if self.__group_type == other.__group_type and self.__parameter == other.__parameter:
                return True

    def __hash__(self):
        return hash((self.__group_type, self.__parameter))

    @property
    def group_type(self) -> GroupType:
        return self.__group_type

    @group_type.setter
    def group_type(self, group_type: GroupType):
        self.__group_type = group_type

    @property
    def parameter(self) -> Parameter:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: Parameter):
        self.__parameter = parameter
