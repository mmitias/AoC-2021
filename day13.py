#Python solution for Day 13 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day13.txt")

def horizFold(coords, foldx):
    newcoords = []
    for row in coords:
        x, y = row
        if x < foldx: 
            newx = (foldx - 1) - x
        else:
            newx = x - (foldx + 1)
        newcoords.append([newx,y])
    return newcoords

def vertFold(coords, foldy):
    newcoords = []
    for row in coords:
        x, y = row
        if y < foldy: 
            newy = (foldy - 1) - y
        else:
            newy = y - (foldy + 1)
        newcoords.append([x,newy])
    return newcoords

coords = []
dedup = []
foldx = 655

for row in inputFile:
    if len(row) > 0 and not row.startswith("fold"):
        x, y = map(int,row.split(","))
        coords.append([x,y])

coords = horizFold(coords,foldx)
for point in coords:
    if point not in dedup:
        dedup.append(point)
        
print(len(dedup))

