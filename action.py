#TODO: Implement base Action class with additional @dataclass classes to enforce specific payloads
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple

class ActionType(Enum):
    SHOOT = auto()
    SELECT = auto()
    MOVE = auto()

@dataclass
class Action:
    type: ActionType

@dataclass
class ShootAction(Action):
    payload: Tuple[float, float]

    def __init__(self, dx:float, dy:float):
        super().__init__(ActionType.SHOOT)
        self.payload = (dx, dy)
