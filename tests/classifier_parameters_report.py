
import sys
import os
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project.function as pf


# dirname = os.path.dirname(__file__)
# data_path = os.path.join(dirname, 'dataset')
data_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset'))
report_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/report/classifier_parameters_report.html'))

data = pf.load_data(data_path)
print(data)

extracted_data=pf.feature_extraction(data)

x_train, x_test, y_train, y_test = pf.train_test_split_local(extracted_data)

names = [
    "MLPClassifier", # Neural network models
    "SVC", # Support Vector Machines
]

classifiers = [
    MLPClassifier(),
    SVC(),
]

parameters = [
    {
        'hidden_layer_sizes': [100], # default : 100
        'max_iter': [600, 800, 1000], # default : 200
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    },
    {
        'C': [0.5, 1.0, 1.5, 2.0], # default=1.0
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    }
]

clf = pf.classifier_parameters_selection(report_path,x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test,names=names,classifiers=classifiers,parameters=parameters)
