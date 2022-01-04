# feature_extraction

import pandas as pd

#   Here is a list of attributes which can be extracted:
#   mean, root mean square, standard deviation, median, quartiles,
#   asymmetry coefficient, Kurtosis, entropy, energy, maxima and minima, coefficient of
#   correlation, histogram, zero crossings, number of peak occurrences.

def feature_extraction(df):
    # calcul un vecteur pour chaque action humaine
    actions_features = {}
    capteur_features = {}
    for subject in range(1,df.max(subject)):
        for experiment in range(1,df.max(experiment)):
            for action in range(1,df.max(action)):
                for signal in df.columns[0:6]:
                    #fetching the vector of the signal
                    vector = df.loc[(df['action'] == action) & (df['subject'] == subject) & (df['experiment'] == experiment), [capteur]]
                    #extracting the features fo the capteur
                    capteur_features[f"mean_{capteur}"] = float(vector.mean())
                    capteur_features[f"std_{capteur}"] = float(vector.std())
                    capteur_features[f"median_{capteur}"] = float(vector.median())
                    capteur_features[f"mad_{capteur}"] = float(vector.mad())
                    capteur_features[f"first_quant_{capteur}"] = float(vector.quantile(q=0.25))
                    capteur_features[f"third_quant_{capteur}"] = float(vector.quantile(q=0.75))
                    capteur_features[f"min_{capteur}"] = float(vector.min())
                    capteur_features[f"max_{capteur}"] = float(vector.max())
                    capteur_features["action"] = action
                # adding the features of an action
                features[(subject, experience, action)] = capteur_features
                # reseting the capteur_features for the next action
                capteur_features
    # Remove missing values
    feature_df = pd.DataFrame.from_dict(features).dropna(axis=1)
    return feature_df
    pass
