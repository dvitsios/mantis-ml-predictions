import sys
import ntpath
import re
import glob


disease = sys.argv[1]

input_file = glob.glob(disease + '/mantis_ml_vs_collapsing.*.csv')[0]
print('Input file:', input_file)


out_file = disease + '/mantis_ml_vs_collapsing.js'
out_fh = open(out_file, 'w')


full_str = ''


# Header: Gene_Name,mantis_ml_rank,mantis_ml_proba,manti_ml_perc,p-val,collapsing_rank,Known_gene
# 	  SCNN1A,9,0.9141234568717511,99.95704928594438,0.0195,213,1.0

cnt = 0
with open(input_file) as fh:
    for line in fh:

        if cnt == 0:
            cnt += 1
            continue

        line = line.rstrip()
        vals = line.split(',')

        known_gene = vals[-1]
        known_gene = known_gene.replace('1.0', 'Yes') 
        known_gene = known_gene.replace('0.0', 'No') 
        vals[-1] = known_gene

        tmp_str = '", "'.join(vals)
        tmp_str = '[ "' + tmp_str + '" ],\n'
        full_str += tmp_str


out_fh.write('var ' + 'mantis_vs_collapsing_json = [\n')
full_str = full_str[:-2] + '\n];'
out_fh.write(full_str)
print(out_file)
