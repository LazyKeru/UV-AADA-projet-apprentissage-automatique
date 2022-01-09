import sys
import os
from joblib import dump
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project.function as pf

data_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset'))
report_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/reports/main.html'))
model_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/models/model.pkl'))

# load data
data = pf.load_data(data_path)
# extract features
extracted_data=pf.feature_extraction(data)
# train and test split
x_train, x_test, y_train, y_test = pf.train_test_split_local(extracted_data)
# standarize the data
x_train, x_test = pf.standarize_data(x_train, x_test)
# makes a report of all the tested classifiers and extracts the best model
clf = pf.classifier_parameters_report(report_path=report_path,x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test)
# saving the best model
dump(clf, model_path)
