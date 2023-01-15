from typing import Protocol

class BaseStage(Protocol):

    def run(self):
        ...
