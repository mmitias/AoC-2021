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

    x1 = min(int(start[0]),int(end[0]))
    y1 = min(int(start[1]),int(end[1]))
    x2 = max(int(start[0]),int(end[0]))
    y2 = max(int(start[1]),int(end[1]))

    if y1 == y2:
        for x in range(x1,x2+1):
            grid[y1][x] += 1

    if x1 == x2:        
        for y in range(y1,y2+1):
            grid[y][x1] += 1

for x in range(rows):
    for y in range(cols):
        if grid[x][y] > 1: counter += 1

print (counter)
    
