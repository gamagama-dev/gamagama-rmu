from gamagama.core import GameSystem
from gamagama.rmu.dice import RMUDiceEngine


class RMUSystem(GameSystem):
    name = "rmu"

    def __init__(self):
        self.dice = RMUDiceEngine()
