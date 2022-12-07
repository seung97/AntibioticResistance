#get list of entities that were in the same paper as a gene

import os, pickle, re

#input files
dirName = "ann\\"
fileNames = os.listdir(dirName)

file = open("hasResultGenes.txt", "r")
lines = file.readlines()
geneNames = {}
for line in lines:
    geneName = line.split()[0]
    geneNames[geneName] = None

samePaper = {}

count = 0
for fileName in fileNames:
    file = open(dirName + fileName, "r", encoding = "utf-8")

    #gather all protein in a paper
    paper = {}
    lines = file.readlines()
    for line in lines:
        tokens = re.split(":|\s|\t", line[:-1])

        if tokens[0][0] == "T":
            if tokens[1] == "Protein":
                name = " ".join(tokens[4:])

                if name not in paper:
                    paper[name] = None

    #apply it to all paper data
    for key in paper:
        if key not in samePaper:
            samePaper[key] = {}

        for key2 in paper:
            if key != key2: #don't count self
                if key2 not in samePaper[key]:
                    samePaper[key][key2] = 1
                else:
                    samePaper[key][key2] += 1

    file.close()

    count += 1
    if count % 1000 == 0:
        print(count) #print progress

print()

#save all pkl
file = open("samePaper.pkl", "wb")
pickle.dump(samePaper, file)
file.close()

#get genes
geneSamePaper = {}
for protein in samePaper:
    if protein in geneNames:
        geneSamePaper[protein] = samePaper[protein]

#save genes txt
file = open("geneSamePaper.pkl", "wb")
pickle.dump(geneSamePaper, file)
file.close()

#todo order
'''
#order
geneSamePaperOrdered = {}
for gene in geneSamePaper:
    geneSamePaperOrdered[gene] = list(sorted(geneSamePaper[gene].items(), key = lambda item: item[1], reverse = True))

#save genes txt
'''
