import sys
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from feature_engineering import refuting_features, polarity_features, hand_features, gen_or_load_feats
from feature_engineering import word_overlap_features
from utils.dataset import DataSet
from utils.generate_test_splits import kfold_split, get_stances_for_folds
from utils.score import report_score, LABELS, score_submission

from utils.system import parse_params, check_version
from sklearn.externals import joblib
import fnc_kfold
import csv


def print_score(predicted,dataset):
    LABELS = ['agree', 'disagree', 'discuss', 'unrelated']
    predicted = [LABELS[int(a)] for a in predicted]

    
    with open('precitions.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=["Claim","Article_body","Stance"])
        
        for i in range(len(predicted)):
             l=predicted[i]
             bodyID= dataset.stances[i]['Body ID']
             b = dataset.articles[bodyID]
             h=dataset.stances[i]['Headline']             
             d={}
             d["Claim"],d['Article_body'],d['Stance']=h,b,l
#             for i in d:
#                 print(type(i))
             writer.writerow(d)
            
        

clf = joblib.load('saved_model.pkl') 
 
new_dataset = DataSet("new")
X_competition, y_competition = fnc_kfold.generate_features(new_dataset.stances,new_dataset, "NEW_TEST_2")
print(X_competition)
predicted = [LABELS[int(a)] for a in clf.predict(X_competition)]



for i in predicted:
    print(i)




 





##print(clf.predict(y_competition))




