#Python solution for Day 11 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def addSurround(lst, x, y, incr):
    maxrow = len(lst[0])-1
    maxcol = len(lst)-1

    if x < maxcol:
        if lst[x+1][y]:  lst[x+1][y] += incr
    
    if y < maxrow:
            if lst[x][y+1]:  lst[x][y+1] += incr
    
    if y < maxrow and x < maxcol:
        if lst[x+1][y+1]:  lst[x+1][y+1] += incr

    if y > 0 and x < maxcol:
        if lst[x+1][y-1]:  lst[x+1][y-1] += incr
                    
    if x > 0 and y < maxrow:
        if lst[x-1][y+1]:  lst[x-1][y+1] += incr
    
    if x > 0:
        if lst[x-1][y]:  lst[x-1][y] += incr
    
    if y > 0:
        if lst[x][y-1]:  lst[x][y-1] += incr

    if y > 0 and x > 0:
        if lst[x-1][y-1]:  lst[x-1][y-1] += incr
        
    return lst

def checkEnergy(lst, max):
    global flashes
    count = 0 
    coords = []
    for idx, row in enumerate(lst):
        for idy, val in enumerate(row):
            if val > max:
                lst[idx][idy] = 0
                count += 1
                coords.append([idx,idy])
    flashes += count

    for coord in coords:
        x = coord[0]
        y = coord[1]
        lst = addSurround(lst, x, y, 1)
    return lst, count

inputFile = readFile("day11.txt")

data = []
flashes = 0

for row in inputFile:
    newrow = list(row)
    newrow = list(map(int, newrow))
    data.append(newrow)

for turn in range(300):
    newdata = []

    for row in data:
        row = [z + 1 for z in row ]
        newdata.append(row)
        data = newdata

    count = 1

    while count:
        data, count = checkEnergy(data, 9)

    checksum = 0
    for row in data:
        checksum += sum(row)

    if checksum == 0: 
        print("found at turn", turn + 1)
        break 

    print(turn)
    for line in data:
        print(line)
    print()

for line in data:
    print(line)
print("flashes", flashes)


    
