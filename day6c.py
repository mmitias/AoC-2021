#Python solution for Day 6 puzzle, using recursion and counting children

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def fishCount(fish,startDay):
    global count
    if startDay<=days:
        children = (days-startDay-fish)/7 + 1
        children += fishCount(8,startDay+fish)
        return children
    else:
        return 0

count = 0
days = 18
inputFile = readFile("stub6.txt")
fishSet = inputFile[0].split(",")
fishsum = len(fishSet)

for idx, fish in enumerate(fishSet):
    fishSet[idx] = int(fish)

for idx, fish in enumerate(fishSet):
    count += fishCount(fish,1)
print count+fishsum
