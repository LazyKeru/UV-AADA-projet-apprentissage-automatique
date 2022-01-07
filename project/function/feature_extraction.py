# feature_extraction

import pandas as pd

#   Here is a list of attributes which can be extracted:
#   mean, root mean square, standard deviation, median, quartiles,
#   asymmetry coefficient, Kurtosis, entropy, energy, maxima and minima, coefficient of
#   correlation, histogram, zero crossings, number of peak occurrences.

def feature_extraction(df):
    # calcul un vecteur pour chaque action humaine
    features = {}
    signal_features = {}
    for subject in range(int(df['subject'].max())):
        for experiment in range(int(df['experiment'].max())):
            for action in range(int(df['action'].max())):
                for signal in df.columns[0:6]:
                    #fetching the vector of the signal
                    vector = df.loc[(df['action'] == action) & (df['subject'] == subject) & (df['experiment'] == experiment), [signal]]
                    #extracting the features fo the signal
                    signal_features[f"mean_{signal}"] = float(vector.mean())
                    signal_features[f"std_{signal}"] = float(vector.std())
                    signal_features[f"median_{signal}"] = float(vector.median())
                    signal_features[f"mad_{signal}"] = float(vector.mad())
                    signal_features[f"first_quant_{signal}"] = float(vector.quantile(q=0.25))
                    signal_features[f"third_quant_{signal}"] = float(vector.quantile(q=0.75))
                    signal_features[f"min_{signal}"] = float(vector.min())
                    signal_features[f"max_{signal}"] = float(vector.max())
                    signal_features["action"] = action
                # adding the features of an action
                print(f"extracting the features for the action {action} of the subject {subject} from the experiment {experiment}")
                # the index is : the action id, the subject id and the experiment id
                features[(subject, experiment, action)] = signal_features
                # reseting the signal_features for the next action
                signal_features = {}
    # Remove missing values
    feature_df = pd.DataFrame.from_dict(features).dropna(axis=1)
    # flips the dataframe
    return feature_df.transpose()
    pass
