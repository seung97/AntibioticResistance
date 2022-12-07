#do additional parsing on the full papers

import os

#input files
dirStart = "pmcParsed\\"
startFileNames = os.listdir(dirStart)

#output folder
endDir = "full\\"

#good type to keep
good = {"front\n" : None, "abstract\n" : None, "paragraph\n" : None}

for startFileName in startFileNames:

    #open files
    startFile = open(dirStart + startFileName, "r", encoding = "utf-8")
    endFile = open(endDir + startFileName, "w", encoding = "utf-8")

    #get type
    lines = startFile.readlines()
    typeLines = lines[1::4]
    textLines = lines[2::4]

    for i in range(len(typeLines)):
        typeLine = typeLines[i]
        textLine = textLines[i]

        if typeLine in good: #if type is good
            endFile.write(textLine)

    startFile.close()
    endFile.close()
