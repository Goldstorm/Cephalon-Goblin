from enum import Enum
from typing import List, Dict, Tuple
from abc import abstractmethod


class WeaponCategory(Enum):
    PRIMARY = 0
    SECONDARY = 1
    MELEE = 2


class Weapon:

    def __init__(self, category: WeaponCategory):
        self.category = category
