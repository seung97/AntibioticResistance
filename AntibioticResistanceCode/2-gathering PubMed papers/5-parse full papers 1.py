#do additional parsing on the full papers

import re

#get file names
pmcIdFileName = "pmc\\pmcAll.txt"
pmcIdFile = open("pmc\\pmcAll.txt", "r")
pmcIds = pmcIdFile.readlines()

#section_type to remove
badSectionType = {"REF": None, "AUTH_CONT": None, "FIG": None, "TABLE": None,
                  "ABBR": None, "ACK_FUND": None, "SUPPL": None, "COMP_INT": None}

for pmcId in pmcIds:
    pmcId = pmcId[:-1]

    #input file
    pmcFullTextFileName = "pmcFull\\" + pmcId + ".txt"
    pmcFullTextFile = open(pmcFullTextFileName, "r", encoding = "utf-8")
    pmcFullTexts = pmcFullTextFile.readlines()

    #output file
    pmcParsedFileName = "pmcParsed\\" + pmcId + ".txt"
    pmcParsedFile = open(pmcParsedFileName, "w", encoding = "utf-8")
    
    for passage in pmcFullTexts:

        #get section_type
        sectionType = re.search('<infon key="section_type">.*?</infon>', passage)
        if not sectionType:
            continue
        
        sectionType = sectionType.group()
        sectionType = sectionType[26:-8]
        if sectionType in badSectionType: #remove bad section_type
            continue

        #get type
        keyType = re.search('<infon key="type">.*?</infon>', passage)
        if not keyType:
            continue
        keyType = keyType.group()
        keyType = keyType[18:-8]

        #get text
        text = re.search('<text>.*?</text>', passage)
        if not text:
            continue
        text = text.group()
        text = text[6:-7]

        #save
        pmcParsedFile.write(sectionType + "\n")
        pmcParsedFile.write(keyType + "\n")
        pmcParsedFile.write(text + "\n")
        pmcParsedFile.write("\n")

    pmcFullTextFile.close()
    
    pmcParsedFile.close()
    
pmcIdFile.close()
