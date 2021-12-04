#Python solution for Day 3 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines
gamma = ""
epsilon = ""
statusCodes = readFile("day3.txt")
for y in range(12):
    columnSum = 0
    for code in statusCodes:
        bit = int(code[y])
        columnSum += bit
    if columnSum > 500: 
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gammaint = int(gamma,2)
epsilonint = int(epsilon,2)
#print (gamma, epsilon)
print(gammaint*epsilonint)