import sys
import ntpath
import re

input_file = sys.argv[1]
print('Input file:', input_file)
out_file = input_file + '.js'
print('Output file:', out_file)

filename = ntpath.basename(input_file)
disease = re.split('_|\.', filename)[1]
print('Disease:', disease)


out_fh = open(out_file, 'w')
out_fh.write('var ' + disease + '_dataset = [\n')

full_out_str = ''

cnt = 0
with open(input_file) as fh:
    for line in fh:
        line = line.rstrip()

        if cnt == 0:
            cnt += 1
            continue

        ranking, gene_name, mantis_proba, mantis_perc, _ = line.split(',')
        ranking = str(int(ranking) + 1)
        # 0,NPHS1,0.933881876,100,

        print(ranking, gene_name, mantis_proba, mantis_perc)

        full_out_str += '[ "' + ranking + '", "' + gene_name + '", "' + mantis_proba + '", "' + mantis_perc + '" ],\n'


full_out_str = full_out_str[:-2] + '\n];'
out_fh.write(full_out_str)
