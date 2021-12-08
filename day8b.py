#Python solution for Day 8 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

inputFile = readFile("day8.txt")

digits = []
count = 0

nine = []
eight = []
seven = []
four = []
one = []

for idx, line in enumerate(inputFile):
    digits.append(line.split("|"))
    temp = digits[idx][1]
    outputlist = temp.split(" ")
    temp = digits[idx][0]
    inputlist = temp.split(" ")

    newnum = ""
    # print inputlist
    # print outputlist

    for digit in inputlist:
        lol = len(digit)

        if lol == 7: eight = list(digit)
        if lol == 3: seven = list(digit)
        if lol == 4: four = list(digit)
        if lol == 2: one = list(digit)

    masked4set = {element for element in four if element not in one}
    masked4 = list(masked4set)
    # print eight
    # print seven
    # print four
    # print one
    # print masked4

    for digit in inputlist:
        lol = len(digit)
        digitlist = list(digit)

        check8 =  all(item in digitlist for item in eight)
        check7 =  all(item in digitlist for item in seven)
        check4 =  all(item in digitlist for item in four)
        check1 =  all(item in digitlist for item in one)
        checkmask = all(item in digitlist for item in masked4)

        if lol == 6 and check7 and check4: 
            nine = list(digit)
            #print "nine", digit
        
        if lol == 6 and check1 and not check4:
            zero = list(digit)
            #print "zero", digit

        if lol == 6 and not check1:
            six = list(digit)
            #print "six", digit

        if lol == 5 and check7:
            three = list(digit)
            #print "three", digit
        
        if lol == 5 and checkmask:
            five = list(digit)
            #print "five", digit
        
        if lol == 5 and not checkmask and not check7:
            two = list(digit)
            #print "two", digit


    for digit in outputlist:
        lol = len(digit)

        if lol == 7: newnum += "8"
        if lol == 3: newnum += "7"
        if lol == 4: newnum += "4"
        if lol == 2: newnum += "1"

        digitlist = list(digit)

        if all(item in nine for item in digitlist) and all(item in digitlist for item in nine): newnum += "9"
        if all(item in six for item in digitlist) and all(item in digitlist for item in six): newnum += "6"
        if all(item in five for item in digitlist) and all(item in digitlist for item in five): newnum += "5"
        if all(item in three for item in digitlist) and all(item in digitlist for item in three): newnum += "3"
        if all(item in two for item in digitlist) and all(item in digitlist for item in two): newnum += "2"
        if all(item in zero for item in digitlist) and all(item in digitlist for item in zero): newnum += "0"

    print (newnum)
    newint = int(newnum)
    count += newint


print (count)