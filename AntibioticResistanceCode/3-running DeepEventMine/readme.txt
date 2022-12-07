copy abstracts and full folders from 2-gathering PubMed papers

run 1-split to batch.py
this splits the data into batches

run DeepEventMine with files from batch# directory as input
save the results into "batch# ann" directory

addtional information on DeepEventMine can be found in readme DeepEventMine.txt

make directory: ann
run 2-gather output.py
this gathers the .ann files for the next step
