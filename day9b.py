#Python solution for 2021 Day 9 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def isLowPoint(row, col):
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
        # print ("lowpoint", point)
        basinsum = basinCount(row,col)
        return basinsum
    
    return 0
        
def basinCount(row,col):
    global data
    point = int(data[row][col])
    # print ("coord", row, col)
    # print (useddata[row][col])
    if useddata[row][col] != 0:
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

        basinsum = 1

        if up<9 and up>point:
            basinsum += basinCount(row-1,col)
            useddata[row-1][col] = 0

        if right<9 and right>point:
            basinsum += basinCount(row,col+1)
            useddata[row][col+1] = 0

        if left<9 and left>point:
            basinsum += basinCount(row,col-1)
            useddata[row][col-1] = 0

        if down<9 and down>point:
            basinsum += basinCount(row+1,col)
            useddata[row+1][col] = 0

        return basinsum
    return 0

inputFile = readFile("day9.txt")

data = []
useddata = []

for row in inputFile:
    data.append(list(row))

maxrow = len(data[0])
maxcol = len(data)
useddata = [ [ [1] for i in range (maxrow) ] for j in range (maxcol)]

basintotal = 0
basinlist = []

for row in range(len(data)):
    for col in range(len(data[row])):

        # for line in useddata:
        #     print (line)
        # print ()
        newbasin = isLowPoint(row,col)
        if newbasin > 0:
            basinlist.append(newbasin)

print (basinlist)
basinlist.sort()
topthree = basinlist[-3:]
print (topthree)
print (topthree[0]*topthree[1]*topthree[2])
