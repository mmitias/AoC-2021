#Python solution for Day 14 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day14.txt")

polymer = list(inputFile[0])
pairmap = {}
charcount = {}

for row in inputFile[2:]:
    key, value = row.split(" -> ")
    pairmap[key] = value

for _ in range(10):
    newpoly = polymer[0]
    for idx, char in enumerate(polymer[:-1], start = 1):
        pair = char + polymer[idx]
        newpoly += pairmap[pair] + polymer[idx]
    polymer = list(newpoly)

for char in polymer:
     charcount[char] = charcount.get(char, 0) + 1

most = max(charcount.values())
least = min(charcount.values())
print(most - least)