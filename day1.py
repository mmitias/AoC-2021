#Python solution for Day 1 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        intLines = [int(x) for x in lines]
        return intLines
counter = 0
sonarReadings = readFile("day1.txt")
for x in range(len(sonarReadings)):
    if x>0:
        if sonarReadings[x]>sonarReadings[x-1]: counter += 1
print (counter)
