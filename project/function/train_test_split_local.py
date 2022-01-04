# train_test_split_local copied from gpascualg/train_test_split.py inspired from sklearn.model_selection.train_test_split

def at(row, i):
    if isinstance(row, pd.Series):
        return row.iloc[i]

    idxs = np.zeros_like(row)
    idxs[i] = 1
    return idxs * row

def train_test_split(row, test_size, random_state):
    data = row[row > 0]
    nonzero = np.where(row)[0]
    n = len(data)
    t = round(n*test_size)

    if n == 0:
        if isinstance(row, pd.Series):
            return pd.Series(name=row.name), pd.Series(name=row.name)

        return np.zeros_like(row), np.zeros_like(row)
    elif t == 0:
        if isinstance(row, pd.Series):
            return at(row, nonzero), pd.Series(name=row.name)

        return (row > 0).astype(int) * row, np.zeros_like(row)

    np.random.seed(random_state)

    idxs = range(n)
    idx = np.random.choice(idxs, size=t,
                           replace=False)

    return (
        at(row, nonzero[list(set(idxs) - set(idx))]),
        at(row, nonzero[idx])
    )

def iter_counts(df):
    if isinstance(df, pd.DataFrame):
        for uid, row in df.iterrows():
            yield uid, row
    else:
        for i in range(df.shape[0]):
            yield i, df[i]

def train_test_split_local(df):
    """
    Cela ne change pas la structure du DataFrame d'origine,
    le divise seulement en 2 sous-DataFrame.

    Ils ont tous les deux le même nombre d'utilisateurs, mais chacun
    on a un ensemble de produits différent de celui-ci

    : param df : DataFrame renvoyé par `build_counts_table`
    : return : Deux DataFrames avec des produits différents
    """
    split = [train_test_split(row, test_size=0.3, random_state=uid) \
                for uid, row in iter_counts(df)]

    train, test = [x[0] for x in split], [x[1] for x in split]

    if isinstance(df, pd.DataFrame):
        train = pd.DataFrame(train).fillna(0)
        test = pd.DataFrame(test).fillna(0)
        return train, test

    return np.array(list(train)), np.array(list(test))

if __name__ == '__main__':
    df_counts_train, df_counts_test = split_train_test(df_counts)
