#Python solution for Day 14 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def countPairs(pairlist):
    global pairs
    for pair in pairlist:
        pairs[pair] += 1

inputFile = readFile("day14.txt")

polymer = inputFile[0]
pairs = {}
chars = {}
addchar = []
pairlist = []
polychars = list(polymer)

for char in polychars:
    if char in chars:
        chars[char] += 1
    else: 
        chars[char] = []
        chars[char] = 1

for idx in range(2, len(inputFile)):
    instruct = inputFile[idx]
    instruct = instruct.split(" -> ")
    key = instruct[0]
    pairs[key] = []
    pairs[key] = 0
    pairlist.append(instruct[0])
    addchar.append(instruct[1])

startpairs = []
depth = 40

for idx, polychar in enumerate(polychars):
    if idx < len(polychars)-1: 
        pair = polychar + polychars[idx+1]
        startpairs.append(pair)

countPairs(startpairs)
temppairs = pairs.copy()

for idx in range(depth):
    for pair, count in pairs.items():
        index = pairlist.index(pair)
        nextchar = addchar[index]
        newpair = pair[0]+nextchar
        newpair2 = nextchar+pair[1]        
        #print(pair, newpair, newpair2, pairs[pair])
        if pairs[pair]:
            temppairs[pair] -= pairs[pair]
            temppairs[newpair] += pairs[pair]
            temppairs[newpair2] += pairs[pair]
            if nextchar in chars:
                chars[nextchar] += pairs[pair]
            else: 
                chars[nextchar] = []
                chars[nextchar] = 1
    pairs = temppairs.copy()

cvalues = chars.values()
most = max(cvalues)
least = min(cvalues)
print(most - least)