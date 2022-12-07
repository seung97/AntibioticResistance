#remove excess abstracts

import os, shutil

#input files
dirStart = "pmidAbstract\\"
startFileNames = os.listdir(dirStart)

#output folder
endDir = "abstracts\\"

#excess Pmid
reffFile = open("excessPmid.txt", "r")
reffList = reffFile.readlines()
reffDic = {key[:-1]: None for key in reffList}
reffFile.close()

for startFileName in startFileNames:
    if startFileName[:-4] not in reffDic: #if abstract should be kept
        shutil.copyfile(dirStart + startFileName, endDir + startFileName)
