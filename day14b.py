#Python solution for Day 14 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

pairs = {}
chars = {}
addchar = []
pairlist = []
depth = 40

inputFile = readFile("day14.txt")
polymer = list(inputFile[0])

for row in inputFile[2:]:
    key, value = row.split(" -> ")
    pairs[key] = 0
    pairlist.append(key)
    addchar.append(value)
    chars[value] = 0

for char in polymer:
    chars[char] += 1

for idx, char in enumerate(polymer[:-1]):
    pair = char + polymer[idx+1]
    pairs[pair] += 1

pairscopy = pairs.copy()

for idx in range(depth):
    for pair, count in pairs.items():
        index = pairlist.index(pair)
        insertchar = addchar[index]
        leftpair = pair[0] + insertchar
        rightpair = insertchar + pair[1]        

        if pairs[pair]:
            pairscopy[pair] -= pairs[pair]
            pairscopy[leftpair] += pairs[pair]
            pairscopy[rightpair] += pairs[pair]
            chars[insertchar] += pairs[pair]

    pairs = pairscopy.copy()

most = max(chars.values())
least = min(chars.values())
print(most - least)