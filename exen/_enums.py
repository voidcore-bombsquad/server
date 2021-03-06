from enum import IntEnum
from sys import maxsize


class Permissions(IntEnum):
    USER: int = 1
    VIP: int = 2
    ADM: int = 4
    MOD: int = 8
    OWN: int = 16
    UNIQUE: int = maxsize

    def __str__(self):
        return self.name

    def __repr__(self):
        return '%s (%s)' % (self.name, self.value)