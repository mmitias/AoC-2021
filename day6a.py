#Python solution for Day 6 puzzle, using a list of fish

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

days = 80
inputFile = readFile("day6.txt")
fishSet = inputFile[0].split(",")

for idx, fish in enumerate(fishSet):
    fishSet[idx] = int(fish)

for day in range(days):
    for idx, fish in enumerate(fishSet):
        if fish == 0:
            fishSet[idx] = 6
            fishSet.append(9)

        else:
            fishSet[idx] -= 1
    #print fishSet
print len(fishSet)