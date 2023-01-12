import pygame
from event_handlers import setup_shoot_event_handler


class Engine:

    def __init__(self):
        self.init_sound()

    def init_sound(self):
        setup_shoot_event_handler()

