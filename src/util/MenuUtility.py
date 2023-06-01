from src.domain.group.GroupType import GroupType


class MenuUtility:

    @staticmethod
    def get_group_type(group_type: GroupType):
        if group_type == GroupType.NONE:
            return "무등급"
        elif group_type == GroupType.GENERAL:
            return "일반"
        elif group_type == GroupType.VIP:
            return "VIP"
        elif group_type == GroupType.VVIP:
            return "VVIP"
