#load_data.py

import numpy as np
import scipy.io as sio
import os

def load_data(path):

    files_list = os.listdir(path)[1:]
    # Our Dataframe will be organized as followed :
    # columns 0-2 : accelerometer (x,y,z)
    # columns 3-5 : gyroscope (x,y,z)
    # column 6 : id of the subject
    # column 7 : id of the experiment
    # column 8 : id of the action
    columns = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z', 'subject', 'experience', 'action']

    # All the data will be put in an array with each item having the following shape : ([A][B][C][D][E][F][G][H][I])
    files_list = np.empty(shape=(1, 9))

    for name_file in list_files:

        name_variable = 'd_iner'
        # Join various path components
        mat_fname=(os.path.join(path, name_file))
        mat_contents = sio.loadmat(mat_fname)
        mat_data = mat_contents[name_variable]

        # each file as a naming convention from which we can extract the id of the subject, of the experience and of the action
        # idAction_idSubject_idExperience
        subject = np.full((mat_data.shape[0], 1), int(name_file.split('_')[1][1:]))
        experience = np.full((mat_data.shape[0], 1), int(name_file.split('_')[2][1:]))
        action = np.full((mat_data.shape[0], 1), int(name_file.split('_')[0][1:]))

        # Join a sequence of arrays along an existing axis
        temp_array = np.concatenate([mat_data, subject, experience, action], axis=1)
        # Join a sequence of arrays along an existing axis
        data_array = np.concatenate((data_array, tmp_array), axis=0)

    # deletes the first column
    data_array = np.delete(data_array, 0, 0)
    df = pd.DataFrame(data_array,  columns=col_names)

    return df
