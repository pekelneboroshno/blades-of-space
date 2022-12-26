from enum import Enum, auto


class Phase(Enum):
    INTRO = auto()
    BEES = auto()


class GameState:
    initial_phase = Phase.BEES
    phase = Phase.BEES
