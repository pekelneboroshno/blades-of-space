import os
from pygame import mixer
from blades_of_space.settings import PROJECT_DIR
from blades_of_space.events import subscribe


mixer.init()


def handler_shoot():
    sound = mixer.Sound(os.path.join(PROJECT_DIR, "sound", "laserShoot.wav"))
    sound.set_volume(0.3)
    mixer.Channel(0).play(sound)


def handle_game_music():
    sound = mixer.Sound(os.path.join(PROJECT_DIR, "sound", "the_last_parsec_1.2.mp3"))
    sound.set_volume(0.5)
    mixer.Channel(1).play(sound)


def setup_shoot_event_handler():
    subscribe("shoot", handler_shoot)


def setup_game_music():
    subscribe("music", handle_game_music)
