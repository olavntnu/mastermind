from a_mastermindGameLogic import GameLogic



failCount = 0
wonCount = 0
guessCount = 0
currentGame = None

def __init__(self):
    
    while True:

        self.currentGame = GameLogic

        if self.currentGame.gameResult[0]:
            self.wonCount += 1
            self.guessCount += self.currentGame.gameResult[1]
        else: self.failCount += 1

        print("Results so far:")
        print("Games Won: " + str(self.wonCount))
        print("Games Lost: " + str(self.failCount))
        print("Average Guesses On Winning Games: " + str(self.guessCount/(self.wonCount)))

        if input("Play Again? (y/n)") == "n":
            break


    


    
