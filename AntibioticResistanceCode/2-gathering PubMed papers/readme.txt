copy the genes folder from 1-gathering genes

make directories: id, pmidAbstract
set the value for fileNums in 1-gather PMID PMC abstract.py
run 1-gather PMID PMC abstract.py
this gathers PMID, PMC, and abstracts from PubMed

make directory: pmc
run 2-prepare PMC.py
this prepares the PMCs for the next step

make directory: pmcFull
set the value for fileNums in 3-gather full paper.py
run 3-gather full paper.py
this gathers the full papers from PubMed

run 4-check gathered PMC.py
this creates a list of PMCs that was successfully gathered

make directory: pmcParsed
run 5-parse full papers 1.py
this pareses the full papers leaving some meta data

make directory: full
run 6-parse full papers 2.py
this pareses the full papers and gets it ready for DeepEventMine

run 7-excess PMID.py
this finds the excess PMID (abstracts) to be removed (abstracts with full paper availble)

make directory: abstracts
run 8-remove excess.py
this removes the excess abstracts

run 9-check genes with results.py
this checks which genes had search results

*there are some hard coded parameters that might need to be changed depending on the data gathered
