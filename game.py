from mastermind import mastermindLogic


class Game:

    solution = []

    def __init__(self):
        self.solution = mastermindLogic.generateCode()
