from a_mastermindGameLogic import MastermindLogic as logic

class Game:

    def __init__(self, custom_code = None):
        if custom_code == None: self.solution = logic.generateCode()
        else: self.solution = logic.generateCode(custom_code)
        self.guesses = []
        self.correct = False
        self.gameOver = False
        self.pins = None

    def checkGameStatus(self):
        return self.gameOver

    def guessCode(self, guess):
        self.pins = None

        self.guesses.append(guess)

        if logic.checkGuess(self.solution, guess):
            self.gameOver = True
            self.correct = True
            #print("Guess number: " + str(len(self.guesses)))
            #print("Congratulations, you guessed correctly!")

        else: 
            if len(self.guesses) >= 10:
                self.gameOver = True
                self.correct = False
                print("Too many guesses, game over!")
            else: 
                self.pins = logic.placePins(self.solution, guess)
                #print("Guess number: " + str(len(self.guesses)))
                #print("Pins: " + str(self.pins))
        
    