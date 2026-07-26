from enum import Enum


class CheckOutcomes(Enum):
    CRIT_FAILURE = ("crit_fail", "Critical Failure")
    FAILURE = ("failure", "Failure")
    SUCCESS = ("success", "Success")
    CRIT_SUCCESS = ("crit_success", "Critical Success")

    def __add__(self, other) -> "CheckOutcomes":
        if not isinstance(other, int):
            return NotImplemented

        members = list(CheckOutcomes)
        current_index = members.index(self)
        new_index = max(0, min(len(members) - 1, current_index + other))
        return members[new_index]

    def __sub__(self, other) -> "CheckOutcomes":
        if not isinstance(other, int):
            return NotImplemented

        return self.__add__(-other)