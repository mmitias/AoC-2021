#Python solution for Day 2 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines
hpos = 0
vpos = 0
subDirections = readFile("day2.txt")
for x in subDirections:
    subMove = x.split()
    #print(subMove)
    direction = subMove[0]
    magnitude = int(subMove[1])
    if direction == "forward": hpos += magnitude
    if direction == "up": vpos -= magnitude
    if direction == "down": vpos += magnitude
    #print (hpos, vpos)
print (hpos*vpos)
