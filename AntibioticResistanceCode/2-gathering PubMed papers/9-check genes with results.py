#get a list of genes that had search results

inputFileNames = ["id\\genes%dMeta.txt" %(i) for i in range(54)]

pmidCount = {}
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()

    for line in lines:
        ids = line.split(" ")
        if len(ids) > 1: #if a gene had a result
            pmidCount[ids[0]] = len(ids) - 1 #save the number of results

    inputFile.close()

#sort
pmidCountList = list(sorted(pmidCount.items(), key = lambda item: item[1], reverse = True))

print("100 genes that gave the most number of results")
print(pmidCountList[:100])
print()
print("number of genes with results", len(pmidCountList))

#save
outputFile = open("hasResultGenes.txt", "w")
for gene, count in pmidCountList:
    outputFile.write(gene + " " + str(count) + "\n")

outputFile.close()
