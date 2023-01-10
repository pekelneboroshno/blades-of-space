from pygame import mixer
from .settings import PROJECT_DIR
from .events import subscribe

# mixer.init()

# mixer.music.load(PROJECT_DIR + "/sound/laserShoot.wav")


def handler_shoot():
    mixer.music.play()


def setup_shoot_event_handler():
    subscribe("shoot", handler_shoot)
