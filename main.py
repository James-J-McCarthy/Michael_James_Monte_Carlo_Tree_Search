import gameState
import random
import time
def gameOn():
    board = gameState.gameState(0b100000000000, 0b100000000000, True, None)
    while board.terminalFlag <= 0:
        if board.playerTurn:
            board = MCTS(board)
            time.sleep(2)
            board.printBoard()
            
        else:
            move = input() # must be row_col
            dl = move[1]
            if dl != ' ':
                for child in board.children:
                    child.printBoard()
                    print("score: ", child.score)
                    print()
                    print()
                
            else: 
                row = int(move[0])
                col = int(move[2])
                board = gameState.gameState(transition(board.bitCode, 1 << row-1 + (col-1) * 4), board.mask, not(board.playerTurn), None)
                board.printBoard()
        print()

def MCTS(current):
    count = 0
    while count < 500:
        leaf = simulate(treeDecision(current))
        backPropogate(leaf[0], current, leaf[1])
        count += 1
    return favoriteChild(current)

def favoriteChild(node):
    fav = None
    for nd in node.children:
        if fav == None:
            fav = nd
        else:
            if nd.terminalFlag > 0:
                fav = nd
                break
            
            if nd.score/(nd.visits) > fav.score/(fav.visits):
                fav = nd
    if fav == None:
        print("fav child error")
    return fav

def backPropogate(start, end, reward):
    pntr = start.parent
    # start.printBoard()
    # print("r: ", reward)
    # print()
    while pntr != end:
        pntr.score += reward
        pntr.visits += 1 
        pntr = pntr.parent

def checkSentinals(bits):
    if len(bin(bits)) == len(bin(0b100010001000)):

        if ((bits & 0b100010001000) > 0b100000000000):
            print("Error with sentinals!")
    else:
        print("length error")

def simulate(node):
    temp = node
    temp.evaluate()
    while temp.terminalFlag == 0:
       
        kids = getChildren(temp)
        randomindex = random.randrange(0, len(kids))
        temp = kids[randomindex]
        checkSentinals(temp.bitCode)

    return [temp, temp.score]

#takes a game.gamestate as input
def treeDecision(node):
    pickedChild = None
    if node.terminalFlag > 0:
        print("Error: treeDecision called on terminal node")
        return None
    for child in getChildren(node):
        #choose child to explore
        if pickedChild == None:
            pickedChild = child
        if child.visits < pickedChild.visits:
            pickedChild = child 
    if pickedChild == None:
        print("Error: no tree decision!")
    return pickedChild

def addChildren(node):
    #adds all children states:
    count = 10 
    length = len(str(bin(node.bitCode)))
    for i in range(3, length):
        if(str(bin(node.bitCode))[i] == '0' and (i != 6 and i != 10)): #skip chars: "0b1", indices 12, 13, 14
            integerMove = 1 << count
            newBitc = transition(node.bitCode, integerMove)
            if(node.playerTurn):
                newmask = transition(node.mask, integerMove)   
            else:
                newmask = node.mask
            node.children.append(gameState.gameState(newBitc, newmask, not(node.playerTurn), node))
        count -= 1
#creates a child board state
def transition(bits, integerMove):
    bitc = bits + integerMove
    return bitc


def getChildren(node):
    if(len(node.children) == 0):
        addChildren(node)
    if(len(node.children) == 0):
        print("error: no children returned!")
    return node.children
        

gameOn()

