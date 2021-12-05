#Python solution for Day 5 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

rows = 1000
cols = 1000
counter = 0

inputFile = readFile("day5.txt")
grid = [[0 for i in range(cols)] for j in range(rows)]

for idx, val in enumerate(inputFile):
    coords = val.split(" -> ")
    start = coords[0].split(",")
    end = coords[1].split(",")

    y = int(start[1])
    x = int(start[0])
    ya = int(end[1])
    xa = int(end[0])
    yinc = 1
    xinc = 1

    if y > ya:
        yinc = -1
    if y == ya:
        yinc = 0

    if x > xa:
        xinc = -1
    if x == xa:
        xinc = 0 
        
    xrang = abs(x-xa)
    yrang = abs(y-ya)
    maxrange = max(xrang,yrang)

    for idx in range(maxrange+1): 
        grid[y][x] += 1
        y += yinc
        x += xinc

for x in range(rows):
    for y in range(cols):
        if grid[x][y] > 1: counter += 1

print counter
    
