make directories: argminer, card

download CARD data (the ones with .fasta files) from the CARD website

move the corresponding files to the card directory
nucleotide_fasta_protein_homolog_model.fasta
nucleotide_fasta_protein_knockout_model.fasta
nucleotide_fasta_protein_overexpression_model.fasta
nucleotide_fasta_protein_variant_model.fasta
nucleotide_fasta_rRNA_gene_variant_model.fasta
protein_fasta_protein_homolog_model.fasta
protein_fasta_protein_knockout_model.fasta
protein_fasta_protein_overexpression_model.fasta
protein_fasta_protein_variant_model.fasta

download ARGminer-A-v1.1.1 from the ARGminer website

move ARGminer-v1.1.1.A.fasta to the argminer directory



make directory: genes
run 1-parse.py
this parses the .fasta files and creates text files containing gene names in the directory gene
