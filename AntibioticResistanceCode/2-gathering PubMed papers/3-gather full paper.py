#get the full papers using PMC

import urllib.request, re, time

#the numbers on the genes file to run
#[0, 1] will run files pmcs0.txt, pmcs1.txt
fileNums = []

pmcFileNames = ["pmc\\pmcs%d.txt" %(i) for i in fileNums]

#create base url
urlFront = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/"
urlBack = "/unicode"

for pmcFileName in pmcFileNames: #for all files
    print(pmcFileName)
    print()

    #input file
    pmcFile = open(pmcFileName, "r")
    pmcs = pmcFile.readlines()

    #output file
    metaFileName = "pmc\\pmcs" + pmcFileName[8:-4] + "Meta.txt"
    metaFile = open(metaFileName, "w")

    #retry
    retry = 0
    
    for pmc in pmcs: #for all pmc
        pmc = pmc[:-1]

        print(pmc)

        #make url
        url = urlFront + pmc + urlBack

        #make request
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
        except urllib.error.HTTPError as err: #404 error, happens when there is no search result
            if err.code != 404:
                print("error:", err.code)
            retry = 0 #don't retry
            time.sleep(1)
            metaFile.write(pmc + "\n")
            continue
        except Exception as err: #other errors
            print("error:", err)

            if retry < 1: #retry once
                retry += 1
                time.sleep(1)
                continue
            else:
                exit()

        retry = 0

        #paper gathered
        metaFile.write(pmc + " yes\n")
        
        #parse paper into passages
        data = data.decode("utf-8")

        data = re.findall("<passage>.*?</passage>", data, re.DOTALL)

        #output file
        fullTextFileName = "pmcFull\\" + pmc + ".txt"
        fullTextFile = open(fullTextFileName, "w", encoding = "utf-8")

        for passage in data: #for each passages
            passage = passage[9:-10]

            #get section_type
            sectionType = re.search('<infon key="section_type">.*?</infon>', passage).group()
            sectionType = sectionType[26:-8]
            if sectionType == "REF" or sectionType == "Table": #don't save REF, Table section_type
                continue

            #save the results
            fullTextFile.write(passage)
            fullTextFile.write("\n")
        
        fullTextFile.close()

        time.sleep(1)

    pmcFile.close()
    metaFile.close()

    print()

    time.sleep(1)
