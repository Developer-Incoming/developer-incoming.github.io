# Deletes any trace of the extensions that I used and edited in the elements of the original html, (ngl I just noticed them).

from os import listdir
from sys import path

folderPath = path[0] + "\\Mocktails"


replaceAnyLineThatContainsWith = [
    # ['  <link crossorigin="anonymous" href="http', ""]
    ['  <link href="css.css?v=20229" rel="stylesheet"/>', '  <link href="../css.css" rel="stylesheet"/>']
]

def replaceWithFunc(filePath):
    file = open(filePath, "r")
    fileLines = file.readlines()
    file.close()

    newFileContent = ""

    for thing in replaceAnyLineThatContainsWith:
        newFileContent = ""

        for line in fileLines:
            if line.startswith(thing[0]):
                newFileContent += thing[1]
            else:
                newFileContent += line
    
    file = open(filePath, "w")
    file.write(newFileContent)
    file.close()

    return filePath

for file in listdir(folderPath):
    print(replaceWithFunc(folderPath + "\\" + file))
    # input() # just in case it doesn't break all the other files, "one by one is good for debugging kids :thumbsup:".
