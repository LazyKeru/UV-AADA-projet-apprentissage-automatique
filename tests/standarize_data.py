
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

print(f"x_train before standarize_data:\n{x_train}")
print(f"x_test before standarize_data:\n{x_test}")

x_train, x_test = pf.standarize_data(x_train, x_test)

print(f"x_train after standarize_data:\n{x_train}")
print(f"x_test after standarize_data:\n{x_test}")
