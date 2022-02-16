from abc import ABC
from dataclasses import dataclass


@dataclass
class Action(ABC):
    pass


@dataclass
class SwitchAgent(Action):
    pass


@dataclass
class Natural(SwitchAgent):
    pass


@dataclass
class ProcedureRequest(Action):
    pass
