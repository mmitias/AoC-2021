#Python solution for Day 13 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def horizFold(coords, foldx):
    newcoords = []
    for row in coords:
        x = row[0]
        y = row[1]
        #print(x,y)
        if x < foldx: 
            newx = (foldx - 1) - x
        else:
            newx = x - (foldx + 1)
        newcoords.append([newx,y])
    return newcoords

def vertFold(coords, foldy):
    newcoords = []
    for row in coords:
        x = row[0]
        y = row[1]
        #print(x,y)
        if y > foldy: 
            newy = foldy - (y - foldy)
        else:
            newy = y
        newcoords.append([x,newy])
    return newcoords

coords = []
folds = []
xmax = 0
ymax = 0

inputFile = readFile("day13.txt")

for row in inputFile:
    if len(row) > 0 and not row.startswith("fold"):
        x, y = row.split(",")
        x = int(x)
        y = int(y)

        coords.append([x,y])
        #print(x,y)

    if row.startswith("fold"):
        parsefold = row.split("=")
        foldline = parsefold[1]
        remainderstr = parsefold[0]
        foldaxis = remainderstr[-1]
        folds.append([foldaxis,foldline])

for fold in folds:
    foldaxis = int(fold[1])
    #print (fold[0],foldaxis)
    if fold[0] == "x":
        coords = horizFold(coords,foldaxis)

    else:
        coords = vertFold(coords,foldaxis)

visibleplot = []

for row in coords:
    x = row[0]
    y = row[1]
    if x > xmax: xmax = x
    if y > ymax: ymax = y

for y in range(ymax+1):
    visiblerow = []
    for x in range(xmax+1):
        visiblerow.append(" ")
    visibleplot.append(visiblerow.copy())

for row in coords:
    x = row[0]
    y = row[1]
    visibleplot[y][x] = "#"
        
for row in visibleplot:
    row.reverse()
    for point in row:
        print(point, end = '')
    print()


