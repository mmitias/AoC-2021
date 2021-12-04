#Python solution for Day 1 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        intLines = [int(x) for x in lines]
        return intLines
counter = 0
sonarReadings = readFile("day1.txt")
for x in range(len(sonarReadings)):
    if x < len(sonarReadings)-3:
        windowA = sonarReadings[x]+sonarReadings[x+1]+sonarReadings[x+2]
        windowB = sonarReadings[x+1]+sonarReadings[x+2]+sonarReadings[x+3]
        print (x, windowA, windowB)
        if windowB > windowA: counter += 1
print (counter)
