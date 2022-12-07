additional information about the output files

proteinData.txt
list of all the proteins
{protein: count}

causeData.txt
list of all the relations
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
