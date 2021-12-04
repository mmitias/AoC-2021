#Python solution for Day 4 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def scanBoard(call, board):
    for x in range(boardSize):
        for y in range(boardSize):
            if board[x][y] == call:
                board[x][y] = "*"
    return board

def checkBoard(board):
    for x in range(boardSize):
        if board[x] == ["*","*","*","*","*"]:
            return 1
        counter = 0
        for y in range(boardSize):
            if board[y][x] == "*": counter += 1
            if counter == 5: 
                return 1

def sumBoard(board):
    boardSum = 0
    for x in range(boardSize):
        for y in range(boardSize):
            if board[x][y] =="*":
                board[x][y] = 0
            boardSum += int(board[x][y])
    return boardSum

inputFile = readFile("day4.txt")

bingoCalls = inputFile[0].split(",")

boardSize = 5
allBoards = []

for x in range (1, len(inputFile), 6):
    curBoard = []

    for y in range(1, boardSize+1):
        curLine = inputFile[x+y].split()
        curBoard.append(curLine)
    allBoards.append(curBoard)

for y in bingoCalls:
    checkResult = 0
    for x in range(len(allBoards)):
        scanBoard(y,allBoards[x])
        checkResult = checkBoard(allBoards[x])
        if checkResult == 1:
            break
    if checkResult == 1:
        break
#print x
#print allBoards[x]
    
newSum = sumBoard(allBoards[x])
#print newSum
#print y
print (newSum*int(y))


