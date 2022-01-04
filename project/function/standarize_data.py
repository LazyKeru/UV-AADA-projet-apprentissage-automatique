def standarize_data(train, test):
    normalized_df = {}
    features_name = list(df.columns)
    features_name.remove('action')
    for name, col in df[features_name].loc[train].items():
        # Moyenne
        mean = col.mean()
        # Ecart-types
        std = col.std()

        new_vector = np.array((df[name] - mean) / std)

        normalized_df[name] = new_vector
    normalized_df['action'] = df['action']
    normalized_df = pd.DataFrame.from_dict(normalized_df)

    return normalized_df
