from .stage1 import Stage
from .stage2 import Stage2
from .stage3 import Stage3
from .stage_protocol import BaseStage


def get_game_stage(player, engine):

    # yield Stage(player, engine)
    # yield Stage2(player, engine)
    yield Stage3(player, engine)


__all__ = ["Stage", "Stage2", "BaseStage"]
