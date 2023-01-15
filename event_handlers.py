from pygame import mixer
from blades_of_space.settings import PROJECT_DIR
from blades_of_space.events import subscribe


def handler_shoot():
    mixer.init()
    mixer.music.load(PROJECT_DIR + "/sound/laserShoot.wav")
    mixer.music.play()


def setup_shoot_event_handler():
    subscribe("shoot", handler_shoot)
