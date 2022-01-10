import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import project.function as pf

# Sample
#            acc_x     acc_y     acc_z      gyr_x      gyr_y      gyr_z  subject  experiment  action
# 0      -0.959717 -0.331299 -0.111084   6.564885   0.335878  -2.809160      1.0         2.0    10.0
# 1      -0.964355 -0.343018 -0.126953  10.809160   1.740458  -3.603053      1.0         2.0    10.0
# 2      -0.976807 -0.370117 -0.140381  12.091603   3.541985  -6.106870      1.0         2.0    10.0
# 3      -0.980713 -0.386230 -0.187500   8.152672   7.725191  -9.679389      1.0         2.0    10.0
# 4      -1.002441 -0.424561 -0.191895   5.282443  14.564885 -14.351145      1.0         2.0    10.0

df = pd.DataFrame({'acc_x': [-0.959717, -0.964355, -0.976807, -0.980713],
                   'acc_y': [-0.331299, -0.343018, -0.370117, -0.386230],
                   'acc_z': [-0.111084, -0.126953, -0.140381, -0.187500],
                   'gyr_x': [6.564885, 10.809160, 12.091603, 8.152672],
                   'gyr_y': [0.335878 , 1.740458, 3.541985, 7.725191],
                   'gyr_z': [-2.809160, -3.603053, -6.106870, -9.679389],
                   'subject': [0.0, 0.0, 1.0, 1.0],
                   'experiment': [0.0, 0.0, 1.0, 1.0],
                   'action': [0.0, 0.0, 1.0, 1.0]})

expected_result = pd.DataFrame({'action': [0.0],
                   'first_quant_acc_x': [-0.9631955],
                   'first_quant_acc_y': [-0.34008825],
                   'third_quant_gyr_x': [9.74809125],
                   'third_quant_gyr_y': [1.389313],
                   'third_quant_gyr_z': [-3.00763325]})

print(f"Dataframe that we need to extract our feature:\n{df}")
print(f"result:\n{pf.feature_extraction(df)}")
print(f"expected result:\n{expected_result}")



# workflow
allowed_error = 0.000001
def test_feature_extraction():
    result = pf.feature_extraction(df)
    assert abs(result.loc[(0,0,0), 'action'] - expected_result.loc[0, 'action']) <= 0.1
    assert abs(result.loc[(0,0,0), 'first_quant_acc_x'] - expected_result.loc[0, 'first_quant_acc_x']) <= allowed_error
    assert abs(result.loc[(0,0,0), 'first_quant_acc_y'] - expected_result.loc[0, 'first_quant_acc_y']) <= allowed_error
    assert abs(result.loc[(0,0,0), 'third_quant_gyr_x'] - expected_result.loc[0, 'third_quant_gyr_x']) <= allowed_error
    assert abs(result.loc[(0,0,0), 'third_quant_gyr_y'] - expected_result.loc[0, 'third_quant_gyr_y']) <= allowed_error
    assert abs(result.loc[(0,0,0), 'third_quant_gyr_z'] - expected_result.loc[0, 'third_quant_gyr_z']) <= allowed_error
