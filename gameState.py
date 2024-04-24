
class gameState:
    def __init__(self, bitCode, p1Mask, turnNumber) -> None:
        self.bitCode = bitCode
        self.mask = p1Mask
        self.turnNumber = turnNumber

    def printToBinary(self):
        print(bin(self.bitCode))

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

            
    



