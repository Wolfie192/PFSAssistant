from enum import Enum


class CheckOutcomes(Enum):
    CRIT_FAILURE = ("crit_fail", "Critical Failure")
    FAILURE = ("failure", "Failure")
    SUCCESS = ("success", "Success")
    CRIT_SUCCESS = ("crit_success", "Critical Success")

    def __init__(self, key: str, display_name: str):
        self._key = key
        self._display_name = display_name

    @property
    def key(self) -> str:
        return self._key

    @property
    def display_name(self) -> str:
        return self._display_name

    @classmethod
    def from_diff(cls, diff: int, nat_20: bool = False, nat_1: bool = False) -> "CheckOutcomes":
        """
        Determined the degree of success based on the difference between the total and the DC.
        Adjusts for natural 20 and natural 1.
        """
        if diff >= 10: outcome = CheckOutcomes.CRIT_SUCCESS
        if diff >= 0: outcome = CheckOutcomes.SUCCESS
        if diff > -10:
            outcome = CheckOutcomes.FAILURE
        else:
            outcome = CheckOutcomes.CRIT_FAILURE

        if nat_20: outcome += 1
        if nat_1: outcome -= 1

        return outcome

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