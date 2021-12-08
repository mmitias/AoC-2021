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
            #print call, board[x][y]
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
    for x in range(boardSize):#
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

boardList = range(len(allBoards))
boardList = list(boardList)
boardNum = 9999

for y in bingoCalls:
    checkResult = 0
    for x in boardList:
        scanBoard(y, allBoards[x])
    for x in boardList:
        checkResult = checkBoard(allBoards[x])
        if checkResult == 1:
            boardList.remove(x)
    if len(boardList) == 1:
        boardNum = boardList[0]
    if len(boardList) == 0:
        break


#print boardNum
#print allBoards[boardNum]

newSum = sumBoard(allBoards[boardNum])
#print newSum
#print y
print (newSum*int(y))


