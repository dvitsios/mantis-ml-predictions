import sys
import ntpath
import re


disease = sys.argv[1]
input_dir = disease + '/ranked-gene-predictions'


input_file = input_dir + '/full_ranked_predictions.csv'
print('Input file:', input_file)
out_proba_file = input_file + '.proba.js'
print('Output proba file:', out_proba_file)
out_perc_file = input_file + '.perc.js'
print('Output percentile file:', out_perc_file)


out_proba_fh = open(out_proba_file, 'w')
out_proba_fh.write('var ' + disease + '_proba_dataset = [\n')
out_perc_fh = open(out_perc_file, 'w')
out_perc_fh.write('var ' + disease + '_perc_dataset = [\n')

full_proba_str = ''
full_perc_str = ''


# Full header:
# Gene_Name,XGBoost_proba,XGBoost_perc,ExtraTrees_proba,ExtraTrees_perc,GradientBoosting_proba,GradientBoosting_perc,RandomForest_proba, RandomForest_perc,DNN_proba,DNN_perc,SVC_proba,SVC_perc,Stacking_proba,Stacking_perc

proba_indexes = [0] + list(range(1, 15, 2))
perc_indexes = [0] + list(range(2, 15, 2))
print(proba_indexes)
print(perc_indexes)



cnt = 0
with open(input_file) as fh:
    for line in fh:
        line = line.rstrip()

        vals = line.split(',')
        proba_vals = [vals[i] for i in proba_indexes]
        perc_vals = [vals[i] for i in perc_indexes]

        if cnt == 0:
            print(proba_vals)
            print(perc_vals)
            cnt += 1
            continue

        print(proba_vals)

        tmp_proba_str = '", "'.join(proba_vals)
        tmp_proba_str = '[ "' + tmp_proba_str + '" ],\n'
        full_proba_str += tmp_proba_str

        tmp_perc_str = '", "'.join(perc_vals)
        tmp_perc_str = '[ "' + tmp_perc_str + '" ],\n'
        full_perc_str += tmp_perc_str


full_proba_str = full_proba_str[:-2] + '\n];'
full_perc_str = full_perc_str[:-2] + '\n];'

out_proba_fh.write(full_proba_str)
out_perc_fh.write(full_perc_str)
