#Python solution for Day 2 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines
hpos = 0
vpos = 0
aim = 0
subDirections = readFile("day2.txt")
for x in subDirections:
    subMove = x.split()
    #print(subMove)
    direction = subMove[0]
    magnitude = int(subMove[1])
    if direction == "forward":
        hpos += magnitude
        vpos += magnitude * aim
    if direction == "up": 
        aim -= magnitude
    if direction == "down":
        aim += magnitude
    #print (hpos, vpos, aim)
print (hpos*vpos)
