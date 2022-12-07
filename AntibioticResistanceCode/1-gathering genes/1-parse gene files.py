#parse the .fasta files and make a list of genes

#argminer

inputFile = open("argminer\\ARGminer-v1.1.1.A.fasta", "r")
outputFile = open("argminer\\argminerGenes.txt", "w")

count = 0
lines = inputFile.readlines()
for line in lines:
    if line[0] == ">": #line containing gene name
        s = line.split("|")[2].strip() #get gene name
        if " " not in s: #remove multi-word gene names
            outputFile.write(s + "\n")
            count += 1

inputFile.close()
outputFile.close()

#card nucleotide

inputFileNames = ["card\\nucleotide_fasta_protein_homolog_model.fasta",
                  "card\\nucleotide_fasta_protein_knockout_model.fasta",
                  "card\\nucleotide_fasta_protein_overexpression_model.fasta",
                  "card\\nucleotide_fasta_protein_variant_model.fasta",
                  "card\\nucleotide_fasta_rRNA_gene_variant_model.fasta"]
outputFile = open("card\\cardGenesNucleotide.txt", "w")

count = 0
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    
    lines = inputFile.readlines()
    for line in lines:
        if line[0] == ">":
            s = line.split("|")[5]
            s = s.split(" ")[0].strip()
            if " " not in s:
                outputFile.write(s + "\n")
                count += 1

    inputFile.close()
    
outputFile.close()

#card protein

inputFileNames = ["card\\protein_fasta_protein_homolog_model.fasta",
                  "card\\protein_fasta_protein_knockout_model.fasta",
                  "card\\protein_fasta_protein_overexpression_model.fasta",
                  "card\\protein_fasta_protein_variant_model.fasta"]
outputFile = open("card\\cardGenesProtein.txt", "w")

count = 0
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    
    lines = inputFile.readlines()
    for line in lines:
        if line[0] == ">":
            s = line.split("|")[3]
            s = s.split(" ")[0].strip()
            if " " not in s:
                outputFile.write(s + "\n")
                count += 1

    inputFile.close()
    
outputFile.close()

#put all the genes in one file

inputFileNames = ["argminer\\argminerGenes.txt",
                  "card\\cardGenesNucleotide.txt",
                  "card\\cardGenesProtein.txt"]

genes = {}
for inputFileName in inputFileNames:
    inputFile = open(inputFileName, "r")
    
    lines = inputFile.readlines()
    for line in lines:
        if line not in genes: #no duplicate names
            genes[line] = None

    inputFile.close()

print("number of genes", len(genes))

outputFile = open("allGenes.txt", "w") #file with all the genes
for gene in genes:
    outputFile.write(gene)
outputFile.close()

#split the genes into files of 100 for later use

num = 0
count = 0
for gene in genes:
    if count == 100:
        outputFile.close()

        count = 0
        num += 1
        
    if count == 0:
        outputFile = open("genes\\genes%d.txt" %(num), "w")
    
    outputFile.write(gene)

    count += 1
    
outputFile.close()
