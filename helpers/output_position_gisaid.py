alignment_file = "../msa_2021-09-08.tar.xz"
import pandas as pd
import lzma
import json
import gzip
from Bio import SeqIO
"""
metadata_file = '../metadata_2021-09-20_06-30.tsv.gz'
handle = gzip.open(metadata_file, 'rt')
df = pd.read_csv(handle, delimiter='\t', index_col=0)

alias_file = "./data/alias_key.json"
alias_dict = json.load(open(alias_file))


def expand_alias(input_string):
    # if input_string is a float return None
    if type(input_string) == float:
        return None
    if "." not in input_string:
        return input_string

    alias, rest = input_string.split('.', 1)

    if alias in alias_dict:
        if alias_dict[alias] == "":
            return alias + '.' + rest
        else:
            return alias_dict[alias] + '.' + rest


df['full_lineage'] = df['pango_lineage'].apply(expand_alias)

#df = df[(df['full_lineage'] + ".").str.startswith('B.1.617.2.')]

df.to_csv("../gisaid_processed_metadata.csv")

reference_file = "./data/reference.fa"
reference = SeqIO.read(reference_file, "fasta")

ref_sequence = str(reference.seq)
"""
handle = lzma.open(alignment_file, 'rt')
for i in range(200):
    handle.seek(1000, 0)
for record in SeqIO.parse(handle, 'fasta'):
    index = 28250 - 1
    residue = str(record.seq)[index]
    print(record.id, index + 1, residue.upper())
