#get a list of all full papers gathered

#gather the PMC
inputFileNames = ["pmc\\pmcs%dMeta.txt" %(i) for i in range(56)]

pmcs = {}
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()

    for line in lines:
        data = line.split(" ")
        if len(data) > 1:
            pmc = data[0]
            
            pmcs[pmc] = None

    inputFile.close()

print("number of full papers gathered", len(pmcs))

#save

outputFileName = "pmc\\pmcAllGathered.txt"
outputFile = open(outputFileName, "w")

for pmc in pmcs:

    outputFile.write(pmc + "\n")

outputFile.close()
