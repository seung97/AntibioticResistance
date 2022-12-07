#split the input data to smaller batches
#big batches runs out of memory

import os, shutil

#number of batches to split to
numDir = 70

#input files
pmcDir = "abstracts\\"
pmidDir = "full\\"

pmcFileNames = os.listdir(pmcDir)
pmidFileNames = os.listdir(pmidDir)

#batch size
pmcLen = len(pmcFileNames) // numDir
pmidLen = len(pmidFileNames) // numDir

for dirIndex in range(numDir):

    #output directory
    dirName = "batch" + str(dirIndex)

    os.mkdir(dirName)
    os.mkdir(dirName + " ann")

    for i in range(pmcLen): #copy full paper
        index = dirIndex * pmcLen + i

        shutil.copyfile(pmcDir + pmcFileNames[index], dirName + "\\" + pmcFileNames[index])

    for i in range(pmidLen): #copy abstract
        index = dirIndex * pmidLen + i

        shutil.copyfile(pmidDir + pmidFileNames[index], dirName + "\\" + pmidFileNames[index])

    #put leftover files to the last directory
    if dirIndex + 1 == numDir:

        for i in range(pmcLen * numDir, len(pmcFileNames)): #copy full paper
            index = i

            shutil.copyfile(pmcDir + pmcFileNames[index], dirName + "\\" + pmcFileNames[index])

        for i in range(pmidLen * numDir, len(pmidFileNames)): #copy abstract
            index = i

            shutil.copyfile(pmidDir + pmidFileNames[index], dirName + "\\" + pmidFileNames[index])
