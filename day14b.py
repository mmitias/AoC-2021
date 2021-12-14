#Python solution for Day 14 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

pairs = {}
chars = {}
pairmap = {}
depth = 40

inputFile = readFile("day14.txt")
polymer = list(inputFile[0])

for row in inputFile[2:]:
    key, value = row.split(" -> ")
    pairs[key] = 0
    pairmap[key] = value
    chars[value] = 0

for char in polymer:
    chars[char] += 1

for idx, char in enumerate(polymer[:-1], start = 1):
    pair = char + polymer[idx]
    pairs[pair] += 1

pairscopy = pairs.copy()

for _ in range(depth):
    for pair, count in pairs.items():
        insertchar = pairmap[pair]
        leftpair = pair[0] + insertchar
        rightpair = insertchar + pair[1]        

        pairscopy[pair] -= pairs[pair]
        pairscopy[leftpair] += pairs[pair]
        pairscopy[rightpair] += pairs[pair]
        chars[insertchar] += pairs[pair]

    pairs = pairscopy.copy()

most = max(chars.values())
least = min(chars.values())
print(most - least)