#Python solution for Day 12 puzzle

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return lines

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path or node.isupper():
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

inputFile = readFile("day12.txt")

data = {}

for row in inputFile:
    key, value = row.split("-")

    if key in data: 
        data[key] += [value]
    else: 
        data[key] = [value]

    if value in data: 
        data[value] += [key]
    else: 
        data[value] = [key]

newpath = find_all_paths(data, 'start', 'end')
print(len(newpath))
