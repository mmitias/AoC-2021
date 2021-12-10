#Python solution for Day 10 puzzle

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

inputFile = readFile("day10.txt")

data = inputFile

openchars = ["(", "{", "<", "["]
closechars = [")", "}", ">", "]"]
scores = dict([(')', 3), (']', 57), ('}', 1197), ('>', 25137)])
syntaxscore = 0

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
                #print (scores[char])
                syntaxscore += scores[char]
                break
                
print (syntaxscore)


