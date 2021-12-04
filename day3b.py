#Python solution for Day 3 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def matchCodes(startBits, codeList):
    newcodes = []
    for code in codeList:
        if code.startswith(startBits):
            newcodes.append(code)
    return newcodes

def mostCommon(codeList, bitPos):
    columnSum = 0
    midpoint = float(len(codeList))/2

    for code in codeList:
        bit = int(code[bitPos])
        columnSum += bit
    if columnSum >= midpoint:
        return "1"
    elif columnSum < midpoint:
        return "0"

def leastCommon(codeList, bitPos):
    columnSum = 0
    midpoint = float(len(codeList))/2

    for code in codeList:
        bit = float(code[bitPos])
        columnSum += bit
    if columnSum >= midpoint:
        return "0"
    elif columnSum < midpoint:
        return "1"

oxygen = ""
scrubber = ""
oxyCodes = readFile("day3.txt")
scrubCodes = readFile("day3.txt")
bitWidth = 12

for y in range(bitWidth):

    if len(oxyCodes)>1:
        oxyResult = mostCommon(oxyCodes,y)
        oxygen += oxyResult
        oxyCodes = matchCodes(oxygen,oxyCodes)

    if len(scrubCodes)>1:
        scrubResult = leastCommon(scrubCodes,y)
        scrubber += scrubResult 
        scrubCodes = matchCodes(scrubber,scrubCodes)

    #print "Oxygen:", oxygen
    #print "Scrubber:", scrubber
    #print (oxyResult,scrubResult)
    #print "OxyCodes:", oxyCodes
    #print "ScrubCodes:", scrubCodes

oxyint = int(oxyCodes[0],2)
scrubint = int(scrubCodes[0],2)

#print (oxyCodes[0], scrubCodes[0])
#print (oxyint, scrubint)
print(oxyint*scrubint)