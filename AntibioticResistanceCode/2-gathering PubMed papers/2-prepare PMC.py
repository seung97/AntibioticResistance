#gather the PMCs

#get a list of unique PMCs
inputFileNames = ["id\\genes%dId.txt" %(i) for i in range(54)]

pmcs = {}
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()

    for line in lines:
        ids = line.split(" ")
        if len(ids) == 2:
            pmc = ids[1]

            if pmc not in pmcs:
                pmcs[pmc] = None

    inputFile.close()

print("number of pmcs", len(pmcs))

#create PMC files of 100 PMC each

num = 0
count = 0
for pmc in pmcs:

    if count == 100:
        count = 0
        num += 1
        outputFile.close()
    
    if count == 0:
        outputFileName = "pmc\\pmcs%d.txt" %(num)
        outputFile = open(outputFileName, "w")

    outputFile.write(pmc)

    count += 1

outputFile.close()
