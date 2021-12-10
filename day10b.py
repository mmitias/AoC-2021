#Python solution for Day 10 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def openChar(closechar):
    i = 0
    listpos = 0
    while (i < len(closechars)):
        if closechars[i] == closechar:
            listpos = i
        i += 1 
    return openchars[listpos]

def closeChar(openchar):
    i = 0
    listpos = 0
    while (i < len(openchars)):
        if openchars[i] == openchar:
            listpos = i
        i += 1 
    return closechars[listpos]

inputFile = readFile("day10.txt")

data = inputFile

openchars = ["(", "{", "<", "["]
closechars = [")", "}", ">", "]"]
scores = dict([(')', 1), (']', 2), ('}', 3), ('>', 4)])

compscores = []
i = 0
brokenrow = 0

for row in data:
    charstack = []
    for char in row:
        #print (charstack)
        if char in openchars:
            charstack.append(char)
        else:
            if charstack[-1] == openChar(char):
                charstack.pop()
                #print ("popped", char)
            else:
                #print (row, "character error", char, "Open Char", openChar(char))
                brokenrow = 1
                break
    linescore = 0
    if len(charstack) and not brokenrow:
        #print (row)
        #print ("incomplete row", i)
        charstack.reverse()
        for char in charstack:
            closechar = closeChar(char)
            linescore = linescore * 5
            linescore += scores[closechar]
            print ("char", closechar, "score", scores[closechar], "linescore", linescore)
    i += 1
    brokenrow = 0
    print ("linescore", linescore)
    if linescore: compscores.append(linescore)
compscores.sort()
print (compscores)
middle = len(compscores)//2
print (compscores[middle])
                


