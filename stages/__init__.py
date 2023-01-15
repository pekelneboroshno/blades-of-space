from .stage1 import Stage
from .stage_protocol import BaseStage


def get_game_stage(player):

    yield Stage(player=player)


__all__ = ["Stage", "BaseStage"]
