addtional information on DeepEventMine

install
install scikit-learn version 0.21.3
brat needs to be installed from https://github.com/nlplab/brat/releases/tag/v1.3_Crunchy_Frog

running
remove the data/my-pubmed/text/processed-text folder each batch
"sh pubmed.sh preprocess my-pubmed" used for preparing data causes an infinite loop on some files
use the outputs in brat/brat-v1.3_Crunchy_Frog/data/my-pubmed-brat
