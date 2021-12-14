#Python solution for Day 14 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day14.txt")

polymer = inputFile[0]
pairs = []
addchar = []
polychars = list(polymer)

for idx in range(2, len(inputFile)):
    instruct = inputFile[idx]
    instruct = instruct.split(" -> ")
    pairs.append(instruct[0])
    addchar.append(instruct[1])

ydx = 0
for idx in range(10):
    newpoly = polychars[0]
    for ydx in range(len(polychars)):
        if ydx < len(polychars)-1:
            pair = polychars[ydx] + polychars[ydx+1]
            index = pairs.index(pair)
            newpoly += addchar[index] + polychars[ydx+1]
    polychars = list(newpoly)
#    print(newpoly)

b = polychars.count("B")
c = polychars.count("C")
n = polychars.count("N")
h = polychars.count("H")
p = polychars.count("P")
k = polychars.count("K")
v = polychars.count("V")
s = polychars.count("S")
zero = polychars.count("O")

most = max([b,c,n,h,p,k,v,s,zero])
least = min([b,c,n,h,p,k,v,s,zero])
print(most - least)