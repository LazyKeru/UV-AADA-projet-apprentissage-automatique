# train_test_split_local copied from gpascualg/train_test_split.py inspired from sklearn.model_selection.train_test_split
import numpy as np
import pandas as pd

def train_test_split_local(data_frame,test_size=0.1):
    """
    Divides the data frame into two parts, and removes their label
    the index is : the action id, the subject id and the experiment id
    the label is the action column
    """
    data_frame_size = len(data_frame)
    # Basic errors:
    if (test_size < 0) and (test_size > 1):
        raise ValueError("test_size needs to be between 0 and 1. I can't give you more than 100%")
        pass
    if data_frame_size == 0:
        raise ValueError("The data frame seems to be empty")
        pass
    # panda has a function to shuffle it's DataFrame
    data_frame = data_frame.sample(frac=1)
    # Spliting the data frame into two with iloc
    split_index = int(data_frame_size*test_size)
    x_train = data_frame.iloc[split_index:]
    x_test = data_frame.iloc[:split_index]
    # popping the column with the labels into new Data Frames
    y_train = x_train.pop('action')
    y_test = x_test.pop('action')
    return x_train, x_test, y_train, y_test
    pass
