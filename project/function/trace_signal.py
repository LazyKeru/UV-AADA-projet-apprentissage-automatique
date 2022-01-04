#trace_signal.py

import sys
import numpy as np
import matplotlib.pyplot as plt

# sensor == accelerometer or gyroscope
def trace_signal(df,sensor,action,subject,experiment):
    if ((sensor=="gyr") or (sensor=="gyroscope")):
        sensor="gyr"
    elif ((sensor=="acc") or (sensor=="accelerometer")):
        sensor="acc"
    else:
        sys.exit("error: trace_signal is expecting one of two sensor")

    # df.loc[row_indexer,column_indexer]
    x = df.loc[(df["action"] == action) & (df["subject"] == subject) & (df["experiment"] == experiment), sensor + "_x"].values
    y = df.loc[(df["action"] == action) & (df["subject"] == subject) & (df["experiment"] == experiment), sensor + "_y"].values
    z = df.loc[(df["action"] == action) & (df["subject"] == subject) & (df["experiment"] == experiment), sensor + "_z"].values

    # fetch the number of values we will place
    nb = len(x)
    # calculating the time axis for which to place the evolution of the different axis (x,y,z)
    time_axis = [x * 0.02 for x in range(0, nb)]

    plt.title("sensor: {sensor}, action: {str(action)}, subject: {str(subject)}, experiment: {str(experiment)}")

    plt.xlabel('Time (s)')

    plt.plot(time_axis, x, 'r')
    plt.plot(time_axis, y, 'g')
    plt.plot(time_axis, z, 'b')

    plt.show()

    pass
