#get PMID where the PMC is gathered
#used to remove abstract if the full paper is available

#files with PMID and PMC
inputFileNames = ["id\\genes%dId.txt" %(i) for i in range(54)]

#get gathered PMC
reffFile = open("pmc\\pmcAllGathered.txt", "r")
reffList = reffFile.readlines()
reffDic = {key: None for key in reffList}
reffFile.close()

pmids = {}
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()

    for line in lines:
        ids = line.split(" ")
        if len(ids) == 2: #if PMID has PMC
            pmid = ids[0]
            pmc = ids[1]

            if pmid not in pmids:
                if pmc in reffDic: #if PMC is gathered
                    pmids[pmid] = None

    inputFile.close()

print("number of pmid to remove", len(pmids))

#save
outputFile = open("excessPmid.txt", "w")
for pmid in pmids:
    outputFile.write(pmid + "\n")

outputFile.close()
