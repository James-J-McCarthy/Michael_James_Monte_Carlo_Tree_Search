
class gameState:
    def __init__(self, bitCode, p1Mask, isP1) -> None:
        self.bitCode = int(bitCode)
        self.mask = int(p1Mask)
        self.playerTurn = isP1

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
        self.printToBinary(winnerPeices)
        self.printToBinary(self.rightShift(winnerPeices, 4))
        self.printToBinary(self.rightShift(winnerPeices, 8))
        return 0 < (winnerPeices & (self.rightShift(winnerPeices, 4)) & self.rightShift(winnerPeices, 8))
        
    def evaluate(self):
        winnerBits = None
        if(self.playerTurn):
            winnerBits = self.bitCode & self.mask
        else:
            winnerBits = self.bitCode & (~self.mask)
        print("entered bits: ")
        self.printToBinary(winnerBits)
        val = -1
        val = self.horizontalWin(winnerBits)
        if val == -1:
            print("eval errro")
        print("val", val)
        return val
    



