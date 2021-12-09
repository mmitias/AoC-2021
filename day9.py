#Python solution for 2021 Day 9 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def isLowPoint(row, col):
    global risklevel
    point = int(data[row][col])

    if row > 0:
        up = int(data[row-1][col])
    else:
        up = 9

    if row < len(data)-1:
        down = int(data[row+1][col])
    else:
        down = 9

    if col > 0:
        left = int(data[row][col-1])
    else:
        left = 9
    
    if col < len(data[row])-1:
        right = int(data[row][col+1])
    else:
        right = 9

    if point < right and point < left and point < up and point < down:
        print ("lowpoint", point)
        risklevel += point +1

inputFile = readFile("day9.txt")

data = inputFile
risklevel = 0 

for row in range(len(data)):
    for col in range(len(data[row])):
        isLowPoint(row,col)
print (risklevel)
