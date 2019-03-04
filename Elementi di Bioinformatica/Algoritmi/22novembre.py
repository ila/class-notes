#!/usr/bin/python

# python 22novembre.py M10051.txt genetic-code.txt  > output.txt

import sys
import re

with open(sys.argv[1],'r') as input_file:
    embl_whole_input = input_file.read()

# ottengo l'identificatore univoco e l'organismo dal record che inizia con ID
header_search = re.search('^ID\s+(\w+).+\s+(\w+);.+\.', embl_whole_input, re.M)
identifier = org = ''
if header_search:
    identifier = header_search.group(1)
    org = header_search.group(2)

# ottengo dal file di input lo start e l'end della CDS
cds_search = re.search('^FT\s+CDS\s+(\d+)\.\.(\d+)\s*$', embl_whole_input, re.M)
cds_start = cds_end = ''

# se esiste la CDS
if cds_search:
    cds_start = cds_search.group(1)
    cds_end = cds_search.group(2)

# ottengo la lista delle righe del file di input che contengono la sequenza nucleotidica
# (escludendo l'intero finale). Il parametro re.M forza la stringa whole_input a essere considerara su piu' righe
seq_row_list = re.findall('^\s+(.+)\s+\d+$', embl_whole_input, re.M)

# ottengo tutti i pezzi della sequenza nucleotidica e li unisco in un'unica stringa
nucleotide_seq = ''.join([''.join(chunk_list) for chunk_list in [row.split() for row in seq_row_list]])

# ottengo la lista dei record relativi alla sequenza della proteina,
# dove ciascun record e' memorizzato come tupla di due elementi di cui il secondo e' un blocco di proteina
prot_row_list = re.findall('^FT\s+(\/translation=\")?([ACDEFGHIKLMNPQRSTVWY]+)\"?$', embl_whole_input, re.M)

# ottengo la sequenza della proteina
protein_from_file = ''.join([row[1] for row in prot_row_list])