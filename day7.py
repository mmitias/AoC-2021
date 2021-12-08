#Python solution for Day 7 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day7.txt")

data = inputFile[0].split(",")

#data = [16,1,2,0,4,2,7,1,2,14]

for idx, hpos in enumerate(data):
    data[idx] = int(hpos)

n = len(data)
data.sort()

distance = 0
  
def fuel(position):
    distance = 0
    for hpos in data:
        distance += abs(position-hpos)
    return distance

highpos = max(data)
lowdist = 9999999999
setsize = len(data)

for idx in range(setsize):
    result = fuel(idx)
    if result<lowdist:
        lowdist = result

print (lowdist)