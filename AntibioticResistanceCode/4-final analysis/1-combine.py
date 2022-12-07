#combine the data in the ann files

import os, pickle, re

#input files
dirName = "ann\\"
fileNames = os.listdir(dirName)

#data to collect
proteinData = {}
causeData = {}

count = 0
for fileName in fileNames:
    file = open(dirName + fileName, "r", encoding = "utf-8")

    #entity tokens
    tokenDic = {}

    lines = file.readlines()
    for line in lines:
        tokens = re.split(":|\s|\t", line[:-1]) #split the line

        if tokens[0][0] == "T": #if data type is T (entity)
            if tokens[1] == "Protein": #if entity is a protein
                name = " ".join(tokens[4:])

                #save
                tokenDic[tokens[0]] = name

                if name not in proteinData:
                    proteinData[name] = 1
                else:
                    proteinData[name] += 1
        
        elif tokens[0][0] == "E": #if data type is E (relation)
            if tokens[4] in tokenDic: #if theme exists
                theme = tokenDic[tokens[4]]

                tokenDic[tokens[0]] = theme
                
                if len(tokens) == 7: #if full relation exists (most relations are incomplete)
                    if tokens[5] == "Cause": #if that relation is a cause relation
                        cause = tokenDic[tokens[6]]

                        #save
                        if cause not in causeData:
                            causeData[cause] = {"positive": {}, "negative": {}}
                        
                        if tokens[1] == "Positive_regulation":
                            regType = "positive"
                        elif tokens[1] == "Negative_regulation":
                            regType = "negative"

                        if theme not in causeData[cause][regType]:
                            causeData[cause][regType][theme] = 1
                        else:
                            causeData[cause][regType][theme] += 1

    file.close()

    count += 1
    if count % 1000 == 0:
        print(count) #print progress

print()

#count
print("number of proteins", len(proteinData))

count = 0
for cause in causeData:
    for regType in causeData[cause]:
        count += len(causeData[cause][regType])
print("number of cause relations", count)

#save pkl
file = open("proteinData.pkl", "wb")
pickle.dump(proteinData, file)
file.close()

file = open("causeData.pkl", "wb")
pickle.dump(causeData, file)
file.close()

#save txt
file = open("proteinData.txt", "w", encoding = "utf-8")
for key in proteinData:
    file.write(key + " " + str(proteinData[key]) + "\n")
file.close()

file = open("causeData.txt", "w", encoding = "utf-8")
for key1 in causeData:
    value1 = causeData[key1]
    for key2 in value1:
        value2 = value1[key2]
        file.write(key1 + " " + key2 + " " + str(value2) + "\n")
file.close()
