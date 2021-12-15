#Python solution for Day 12 puzzle, part 2

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def canVisit(node, path, max):
    counter = 0
    doublevisits = 0 

    if node.isupper():
        return 1

    for element in path: 
        if path.count(element) > 1 and element.islower():
            doublevisits += 1

    if doublevisits > 2:
        return 0

    for idx in range(len(path)):
        if (path[idx] == node):
            counter += 1

        if counter == max or node == "start":
            return 0
    return 1

def findPaths(graph, start, end):

    q = []
    path = []
    allpaths = []

    path.append(start)
    q.append(path.copy())
     
    while q:
        path = q.pop(0)
        lastnode = path[len(path) - 1]
 
        if (lastnode == end):
            #print(path)
            allpaths.append(path)

        for i in range(len(graph[lastnode])):
            if (canVisit(graph[lastnode][i], path, 2)):
                newpath = path.copy()
                newpath.append(graph[lastnode][i])
                q.append(newpath)
    return allpaths

inputFile = readFile("day12.txt")

data = {}

for idx, row in enumerate(inputFile):
    key, value = row.split("-")

    if key in data: 
        data[key] += [value]
    else: 
        data[key] = [value]

    if value in data: 
        data[value] += [key]
    else: 
        data[value] = [key]

data["end"] = []

newpath = findPaths(data, 'start', 'end')
print(len(newpath))
