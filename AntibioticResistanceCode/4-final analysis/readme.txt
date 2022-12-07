copy hasResultGenes.txt file from 2-gathering PubMed papers
copy ann folder from 3-running DeepEventMine

run 1-combine.py
this combines the data in the .ann files

run 2-common.py
this filters the data to be about genes and orders it

run 3-samePaper.py
this gatheres data on which proteins occurs together in the same paper



additional information about the output files

proteinData.pkl
proteinData.txt
dictionary of all the proteins
{protein: count}

causeData.pkl
causeData.txt
dictionary of all the relations
{protein1: {positive: {protein2: count}},
           {negative: {protein2: count}}}
positive means protein1 has a positive effect on protein2
negative means protein1 has a negative effect on protein2

geneData.txt
list of all genes found
gene count

geneToProtein.txt
dictionary of gene to protein relations
gene positive {protein: count}
gene negative {protein: count}

samePaper.pkl
dictionary of proteins that comes out in the same paper with a protein
(it is a .pkl file because the file is very large)
{protein1: {protein2: count}}

geneSamePaper.pkl
dictionary of proteins that comes out in the same paper with a gene
(it is a .pkl file because the file is very large)
{gene: {protein: count}}

*protein includes gene
