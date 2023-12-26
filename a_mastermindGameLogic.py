import random as r
import copy

class MastermindLogic: 
    
    #Dictionary containing numbers and mapping to colours
    colours = {1:'Green', 2:'Blue', 3:'Yellow', 4:'White', 5:'Purple', 6:'Red'}

    @staticmethod
    def generateCode():
        return [r.randint(1,6),
                r.randint(1,6),
                r.randint(1,6),
                r.randint(1,6)
               ]
    @staticmethod
    def checkGuess(code, guess):
        return code == guess

    @staticmethod
    def placePins(code, guess):

        whiteCount = 0

        subtractedList = [x-y for x,y in zip(code,guess)]

        newCode = []
        newGuess = []

        for i in range(len(subtractedList)):
            if subtractedList[i] != 0:
                newCode.append(code[i])
                newGuess.append(guess[i])
        while len(newGuess) != 0:
            if newGuess[0] in newCode:
                whiteCount += 1
                newCode.remove(newGuess[0])
            newGuess.pop(0)

    
        return [subtractedList.count(0), whiteCount] #Black Pins, White Pins (Correct Pin/Correct Pos, Correct Pin/Wrong Pos)

class GameLogic:

    solution = []
    guesses = []
    correct = False

    gameResult = ()

    def __init__(self):
        self.solution = MastermindLogic.generateCode()
        self.guesses = []
        self.correct = False
        
        print(self.solution)

        self.playGame()
    
    def playGame(self):

        while True:
            if len(self.guesses) == 10: 
                print ("Too many guesses, you lost")
                break

            self.guesses.append(self.askForGuess())

            if MastermindLogic.checkGuess(self.solution, self.guesses[-1]):
               print("Correct, you win") 
               self.correct = True
               break
            else: print(MastermindLogic.placePins(self.solution, self.guesses[-1]))
        self.gameResult = (self.correct, len(self.guesses))
        


    def askForGuess(self):
        print ("Input int guess:")

        guess = []

        for i in range (4):
            guess.append(int(input()))

        return guess
    
    