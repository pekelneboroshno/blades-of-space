from .stage1 import Stage
from .stage2 import Stage2
from .stage3 import Stage3
from .stage4 import Stage4
from .stage5 import Stage5
from .bridge import BridgeStage
from .stage_protocol import BaseStage
from .title_screen import TitleScreen
from .last_screen import LastScreen


def get_game_stage(player, engine):

    yield TitleScreen(player, engine)
    yield BridgeStage(player, engine)
    yield Stage(player, engine)
    yield BridgeStage(player, engine)
    yield Stage2(player, engine)
    yield BridgeStage(player, engine)
    yield Stage3(player, engine)
    yield BridgeStage(player, engine)
    yield Stage4(player, engine)
    yield BridgeStage(player, engine)
    yield Stage5(player, engine)
    yield LastScreen(player, engine)


__all__ = ["Stage", "Stage2", "Stage3", "Stage4",  "Stage5", "BaseStage", "TitleScreen"]
