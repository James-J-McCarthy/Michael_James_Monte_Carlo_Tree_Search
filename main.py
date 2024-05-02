import gameState

gs = gameState.gameState(0b00101100110, 0b00001100100, True)
# gs.printBoard()
# gs.evaluate()
gs = gameState.gameState(0b10101010101, 0b10001010100, True)
gs.printBoard()
gs.evaluate()

print("1100 & 100: ", bin(int(0b1000 / 2**1)))

