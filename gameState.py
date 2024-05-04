
class gameState:
    def __init__(self, bitCode, p1Mask, isP1, parent) -> None:
        self.winScore = 1
        self.tieScore = .5
        self.loseScore = -1.1
        self.bitCode = int(bitCode)
        self.mask = int(p1Mask)
        self.playerTurn = isP1
        self.score = 0
        self.visits = 0
        self.terminalFlag = self.evaluate()
        self.parent = parent
        self.children = []
        
        
        
 
    def printToBinary(self, bits):
        print(bin(bits))

    def rightShift(self, bits, n):
        bits = int(bits / 2 ** n)
        return bits
    
    # call like: list = placeChar(list, "x", 2)
    def placeCharInLine(self, stringy, character, index):
        stringList = list(stringy)
        stringList[index] = character
        new_string = "".join(stringList)
        return new_string

    # returns 0 if empty, 'x' if X, 'o' if O
    def checkSquare(self, row, col):
        if(self.bitCode & 1 << ((row)+(col*4))):
            if(self.mask & 1 << ((row)+(col*4))):
                return 'x'
            return 'o'
        return None
    
    def printBoard(self):
        for i in range(3):
            line = "|___|___|___|"
            for j in range(3):
                peice = self.checkSquare(i, j)
                if peice != None:
                    # print("i: ", i, " j: ", j)
                    line = self.placeCharInLine(line, peice, (j*4)+2)
            print(line, "\n")
    
    
    def horizontalWin(self, winnerPeices):
        winnerPeices -= 0b100000000000
        if 0 < (winnerPeices & (self.rightShift(winnerPeices, 4)) & self.rightShift(winnerPeices, 8)):
            self.updateScore()
            return 1
        else:
            return 0
    
    def verticalWin(self, winnerPeices):
        winnerPeices -= 0b100000000000
        if 0 < (winnerPeices & (self.rightShift(winnerPeices, 1)) & self.rightShift(winnerPeices, 2)):
            self.updateScore()
            return 1
        else:
            return 0
        
    def updiagWin(self, winnerPeices):
        winnerPeices -= 0b100000000000
        if 0 < (winnerPeices & (self.rightShift(winnerPeices, 5)) & self.rightShift(winnerPeices, 10)):
            self.updateScore()
            return 1
        else:
            return 0
    
    def downdiagWin(self, winnerPeices):
            winnerPeices -= 0b100000000000
            if 0 < (winnerPeices & (self.rightShift(winnerPeices, 3)) & self.rightShift(winnerPeices, 6)):
                self.updateScore()
                return 1
            else:
                return 0
            
    def checkDraw(self, winnerPeices):
        if winnerPeices > 0b111101110110:
            # print("winnerpeices: ", bin(winnerPeices))
            # print('Game ends in draw')
            self.score = .5
            return 1 #flag still goes to 1: can only be -1 sentinal, 0 by default or 1
        else:
            return 0

    def evaluate(self):
        winnerBits = None
        if(not(self.playerTurn)):
            winnerBits = self.mask
        else:
            winnerBits = self.bitCode - self.mask + 0b100000000000
        val = -1
        val = max(self.horizontalWin(winnerBits),
                  self.updiagWin(winnerBits),
                  self.downdiagWin(winnerBits),
                  self.verticalWin(winnerBits))
        if val < 1:
            val = self.checkDraw(self.bitCode)
    
        if val == -1:
            print("eval errro")
        return val

    def updateScore(self):
        if(self.playerTurn):
            self.score = self.loseScore
        else:
            self.score = self.winScore

