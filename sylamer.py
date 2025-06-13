import argparse
from Bio import SeqIO
import os

# Step 1: Get user input
parser = argparse.ArgumentParser(description='takes user input')

parser.add_argument('rank', help='ranked genes file')
parser.add_argument('fasta', help='fasta utr file')

"""
parser.add_argument('output', required=True)
"""

args = parser.parse_args()

# Step 2: put ranked genes into list
rank = args.rank
with open(rank) as file:

    # gets all ids into a list
    ranked_id = [line.strip().split()[0] for line in file if line.strip()]

# Step 3: gene id as key, utr seq as value
id_to_utr = {}
fasta = args.fasta
seq_objects = SeqIO.parse(fasta,'fasta')

for seq in seq_objects:
    id_to_utr[str(seq.id)] = str(seq.seq)
    print(len(id_to_utr[str(seq.id)]))