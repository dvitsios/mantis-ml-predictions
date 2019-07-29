import pandas as pd
import sys
import glob
import ntpath


top_clf_per_disease = { 'ALS': 'ExtraTrees', 
			'Alzheimers': 'SVC',
			'Autism': 'ExtraTrees',
			'CKD': 'XGBoost', 
			'Epilepsy': 'XGBoost', 
			'GMS': 'GradientBoosting'}


if __name__ == '__main__':

    disease = sys.argv[1]

    input_dir = disease + '/ranked-gene-predictions'
    pred_tables = []
    classifiers = ['XGBoost', 'ExtraTreesClassifier', 'GradientBoostingClassifier', 'RandomForestClassifier', 'DNN', 'SVC', 'Stacking']

    for clf in classifiers:
        tmp_file = input_dir + '/' + clf + '.All_genes.mantis-ml_percentiles.csv'
        pred_tables.append(tmp_file)
    print(pred_tables)

    full_df = pd.DataFrame()


    for clf_table_file in pred_tables:

        clf = ntpath.basename(clf_table_file).split('.')[0]
        clf = clf.replace('Classifier', '')
        print(clf)

        try:
            clf_df = pd.read_csv(clf_table_file, index_col=0)
            clf_df.columns = ['Gene_Name',  clf + '_proba', clf + '_perc']


            if full_df.shape[0] > 0:
                full_df = pd.merge(full_df, clf_df, left_on='Gene_Name', right_on='Gene_Name')
            else:
                full_df = clf_df
        except:
            full_df[clf + '_proba'] = '-'
            full_df[clf + '_perc'] = '-'


    full_df.sort_values(by=top_clf_per_disease[disease] + '_proba', ascending=False, inplace=True)
    full_df = full_df.round(3)
    print(full_df.head())
    print(full_df.shape)

    full_df.to_csv(input_dir + '/full_ranked_predictions.csv', index=None)
    print('Saved to ' + input_dir + '/full_ranked_predictions.csv')
