def standarize_data(train, test):
    """
    standarize the training and test data set
    :param DataFrame train: train dataset
    :param DataFrame test: test dataset
    :return: sends back the standarized data (standarized_df_train, standarized_df_test)
    """
    standarized_df_train = {}
    standarized_df_test = {}
    features_name = list(df.columns)
    for name, col in train[features_name].items():
        # Moyenne
        mean = col.mean()
        # Ecart-types
        std = col.std()
        standarized_df_train[name] = np.array((train[name] - mean) / std)
        standarized_df_test[name] = np.array((test[name] - mean) / std)
    standarized_df_train = pd.DataFrame.from_dict(standarized_df_train)
    standarized_df_test = pd.DataFrame.from_dict(standarized_df_test)
    return standarized_df_train, standarized_df_test
