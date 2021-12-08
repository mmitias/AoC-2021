#Python solution for Day 8 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day8.txt")

digits = []
count = 0

for idx, line in enumerate(inputFile):
    digits.append(line.split("|"))
    temp = digits[idx][1]
    outputlist = temp.split(" ")
    for digit in outputlist:
        lol = len(digit)
        if lol == 2 or lol == 3 or lol == 4 or lol == 7: count +=1
        #print outputlist

print count