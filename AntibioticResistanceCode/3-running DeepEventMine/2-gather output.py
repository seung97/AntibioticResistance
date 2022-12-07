#gather all non-empty annotation files

import os, shutil

#number of batches
numDir = 70

#directory names
dirNameStart = "batch"
dirNameEnd = " ann\\"

endDirName = "ann\\"

#count
fileCount = 0
emptyFileCount = 0

for dirIndex in range(numDir):

    #file name
    dirName = dirNameStart + str(dirIndex) + dirNameEnd

    fileNames = os.listdir(dirName)

    for fileName in fileNames:
        if fileName[-3:] == "ann":

            fileCount += 1

            if os.path.getsize(dirName + fileName) == 0: #if annotation file empty
                emptyFileCount += 1
            else: #if not empty
                shutil.copyfile(dirName + fileName, endDirName + fileName)

print("total count", fileCount)
print("non-empty count", fileCount - emptyFileCount)
print("empty count", emptyFileCount)
