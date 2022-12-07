#make filtered and sorted list of gene data

import pickle

#input data
file = open("proteinData.pkl", "rb")
proteinData = pickle.load(file)
file.close()

file = open("causeData.pkl", "rb")
causeData = pickle.load(file)
file.close()

file = open("hasResultGenes.txt", "r")
lines = file.readlines()
geneNames = {}
for line in lines:
    geneName = line.split()[0]
    geneNames[geneName] = None

#geneData

#get genes
geneData = {}
for protein in proteinData:
    if protein in geneNames:
        geneData[protein] = proteinData[protein]

#order
geneDataList = list(sorted(geneData.items(), key = lambda item: item[1], reverse = True))

print("100 most common genes")
print(geneDataList[:100])
print()

#save
file = open("geneData.txt", "w", encoding = "utf-8")
for gene, count in geneDataList:
    file.write(gene + " " + str(count) + "\n")
file.close()

#geneCauseData

#get genes
geneCauseData = {}
for protein in causeData:
    if protein in geneNames:
        geneCauseData[protein] = causeData[protein]

#count number of relations
geneCauseDataCount = {}
for gene in geneCauseData:
    count = 0
    for relationType in causeData[gene]:
        count += len(geneCauseData[gene][relationType])
    geneCauseDataCount[gene] = count

#order
geneCauseDataList = list(sorted(geneCauseDataCount.items(), key = lambda item: item[1], reverse = True))

print("genes and number of relations")
print(geneCauseDataList)
print()

print("gene with most number of relations")
print(geneCauseDataList[0][0], geneCauseData[geneCauseDataList[0][0]])
print()

#save
file = open("geneToProtein.txt", "w", encoding = "utf-8")
for gene, count in geneCauseDataList:
    value1 = geneCauseData[gene]
    for key in value1:
        value2 = value1[key]
        file.write(gene + " " + key + " " + str(value2) + "\n")
file.close()

#todo protein to gene

#stat
bothCount = 0
onlyGeneCount = 0
for gene in geneNames:
    if gene in proteinData:
        bothCount += 1
    else:
        onlyGeneCount += 1

onlyProteinCount = len(proteinData) - bothCount

print("number of genes found in the annotations", bothCount)
print("number of genes not found in the annotations", onlyGeneCount)
print("number of non-gene proteins in the annotations", onlyProteinCount)
print()

bothCount = 0
foundDic = {}
for key in causeData:

    if key in geneNames:
        if key not in foundDic:
            foundDic[key] = None
    
    for relationType in causeData[key]:
        for protein in causeData[key][relationType]:
            if protein in geneNames:
                if protein not in foundDic:
                    foundDic[protein] = None

print("number of genes that is found in a relation", len(foundDic))
