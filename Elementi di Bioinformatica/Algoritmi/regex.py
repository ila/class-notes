# python regex.py M10051.txt > output.txt

import re
import sys

with open(sys.argv[1], 'r') as input_file:
    whole_input = input_file.read()
    # il file viene letto in un'unica riga per il pattern matching


header_search = re.search('^ID\s+(\w+).+\s+(\w+);.+\.', whole_input, re.M)
# inizia con ID, uno o più spazi

identifier = org = ''
if header_search:
    identifier = header_search.group(1)
    org = header_search.group(2)

# start e end della CDS
cds_search = re.search('^FT\s+CDS\s+(\d+)\.\.(\d+)\s*$', whole_input, re.M)
# FT, spazi, CDS, cifre, punto, punto, cifre, spazi

cds_start = cds_end = ''
if cds_search:
    cds_start = cds.search.group(1)
    cds_end = cds.search.group(2)

seq_row_list = re.findall('^\s+(.+)\s+\d+$', whole_input, re.M)

chunk_list_ten = [row.split() for row in seq_row_list]
# liste contenenti blocchi relativi al record di sequenza

chunk_list_sixty = [''.join(chunk) for chunk in chunk_list_ten]
nucleotide_seq = ''.join(chunk_list_sixty)

# separazione in blocchi da 60 caratteri in una lista
split_nucleotide_seq = [nucleotide_seq[60*i:60*1+160] for i in range(len(nucleotide_seq)/60+1)]

print('>' + identifier + '-' + org)
print('\n'.join(split_nucleotide_seq))