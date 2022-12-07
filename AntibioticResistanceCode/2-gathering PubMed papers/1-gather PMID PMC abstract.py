#gather PMID PMC and abstracts

import urllib.request, re, time

#the numbers on the genes file to run
#[0, 1] will run files genes0.txt, genes1.txt
fileNums = []

#additional search terms
additionalTerms = ["antibiotic", "gene"]

geneFileNames = ["genes\\genes%d.txt" %(i) for i in fileNums]

urlBase = "https://pubmed.ncbi.nlm.nih.gov/?format=pubmed&size=200&term="
advancedSearchStr = "%5BTitle%2FAbstract%5D"

#create base url
urlFront = urlBase
for additionalTerm in additionalTerms:
    urlFront = urlFront + additionalTerm + advancedSearchStr + "+AND+"

urlBack = advancedSearchStr

for geneFileName in geneFileNames: #for all files
    print(geneFileName)
    print()

    #output files
    idFileName = "id\\" + geneFileName[6:-4] + "Id.txt"
    metaFileName = "id\\" + geneFileName[6:-4] + "Meta.txt"

    geneFile = open(geneFileName, "r")
    idFile = open(idFileName, "w")
    metaFile = open(metaFileName, "w")

    genes = geneFile.readlines()
    for gene in genes: #for all genes
        gene = gene[:-1]
        
        metaFile.write(gene)

        #for retrying when request fails
        retry = 0

        #for searchs with multiple result pages
        page = 1
        while page != None:

            print(gene)

            #make url
            url = urlFront + gene + urlBack
            if page != 1:
                url = url + "&page=" + str(page)

            #make request
            try:
                with urllib.request.urlopen(url) as response:
                    data = response.read()
            except urllib.error.HTTPError as err: #404 error, happens when there is no search result
                if err.code != 404:
                    print("error:", err.code)
                retry = 0 #don't retry
                time.sleep(1)
                break
            except Exception as err: #other errors
                print("error:", err)

                if retry < 1: #retry once
                    retry += 1
                    time.sleep(1)
                    continue
                else:
                    exit()

            retry = 0

            #parse the data into individual papers
            data = data.decode("utf-8") + "\r\n\r\n"

            data = re.findall("PMID-.*?\r\n\r\n", data, re.DOTALL)

            #handle cases with multiple pages
            if len(data) == 200:
                page += 1
            else:
                page = None

            for paper in data: #for each paper

                #parse

                #get abstract
                abstract = re.search("AB  - .*?FAU -", paper, re.DOTALL)
                if abstract: #only use papers with an abstract
                    abstract = abstract.group()

                    abstractList = abstract.split("\r\n")
                    while (len(abstractList) != 1) and (abstractList[-1][0] != " "):
                        abstractList.pop()

                    abstractListTemp = []
                    for abstractLine in abstractList:
                        abstractListTemp.append(abstractLine[6:])

                    abstract = "".join(abstractListTemp)

                    #get title
                    title = re.search("TI  - .*?PG  -", paper, re.DOTALL)
                    if not title:
                        title = re.search("TI  - .*?LID -", paper, re.DOTALL)
                        if not title:
                            title = re.search("TI  - .*?BTI -", paper, re.DOTALL)
                            if not title:
                                continue
                    title = title.group()

                    titleList = title.split("\r\n")
                    while (len(titleList) != 1) and (titleList[-1][0] != " "):
                        titleList.pop()

                    titleListTemp = []
                    for titleLine in titleList:
                        titleListTemp.append(titleLine[6:])

                    title = "".join(titleListTemp)

                    #get PMID
                    pmid = re.search("PMID- [0-9]+", paper).group()
                    pmid = pmid[:5] + pmid[6:]

                    #get PMC
                    pmc = re.search("PMC[0-9]+", paper)

                    #save the results
                    metaFile.write(" " + pmid)
                    
                    idFile.write(pmid)
                    
                    if pmc:
                        pmc = pmc.group()

                        idFile.write(" " + pmc)

                    idFile.write("\n")

                    abstractFile = open("pmidAbstract\\%s.txt" %(pmid), "w", encoding = "utf-8")
                    abstractFile.write(title + "\n")
                    abstractFile.write(abstract + "\n")
                    abstractFile.close()

            time.sleep(1)

        metaFile.write("\n")

    geneFile.close()
    idFile.close()
    metaFile.close()

    print()

    time.sleep(1)
