#Python solution for Day 6 puzzle, works for part 1 and part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

days = 256

inputFile = readFile("day6.txt")
fishSet = inputFile[0].split(",")
fishsum = len(fishSet)

dayinc = [0]*days
count = fishsum

for idx, fish in enumerate(fishSet):
    day = int(fish)
    dayinc[day] += 1

count += sum(dayinc)

for day in range(8,days):
    newfish = dayinc[day-7] + dayinc[day-9]
    dayinc[day] += newfish
    count += newfish

print (count)

