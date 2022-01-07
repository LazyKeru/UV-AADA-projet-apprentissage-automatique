
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import project.function as pf


# dirname = os.path.dirname(__file__)
# data_path = os.path.join(dirname, 'dataset')
data_path =(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset'))

data = pf.load_data(data_path)
print(data)

pf.trace_signal(data, 'acc', 10.0, 1.0, 2.0)

extracted_data=pf.feature_extraction(data)
print(extracted_data)
print(extracted_data.columns)


x_train, x_test, y_train, y_test = pf.train_test_split_local(extracted_data)
print("data train:")
print(x_train)
print("label train:")
print(y_train)
print("data test:")
print(x_test)
print("label test:")
print(y_test)
