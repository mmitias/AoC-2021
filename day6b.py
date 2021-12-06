#Python solution for Day 6 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def fishCount(fish,startDay):
    global count
    for day in range(startDay+fish,days+1,7):
        count += 1
        fishCount(9,day)
    return count

count = 0
days = 80
inputFile = readFile("day6.txt")
fishSet = inputFile[0].split(",")
childsum = 0
fishsum = len(fishSet)

for idx, fish in enumerate(fishSet):
    fishSet[idx] = int(fish)

for idx, fish in enumerate(fishSet):
    fishCount(fish,1)

print count+fishsum