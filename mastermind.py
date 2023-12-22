import random as r
import copy

class mastermindLogic: 
    
    #Dictionary containing numbers and mapping to colours
    colours = {1:'Green', 2:'Blue', 3:'Yellow', 4:'White', 5:'Purple', 6:'Red'}


    def generateCode(self):
        return [r.randint(1,6),
                r.randint(1,6),
                r.randint(1,6),
                r.randint(1,6)
               ]

    def checkGuess(code, guess):
        return code == guess

    
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

