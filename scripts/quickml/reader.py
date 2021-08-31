#!/usr/bin/python3

def read_csv(pd, np, path: str, percentage: int, delimiter: str = ",", chunk_size: int=100000, nrows: int = None):
    data = pd.DataFrame()

    for chunk in pd.read_csv(path, sep=delimiter, nrows=nrows, chunksize=chunk_size):
        actual_chunk_size = chunk.shape[0]
        random_size = int(actual_chunk_size * (percentage / 100))
        random_indexes = np.random.default_rng().choice(chunk.index, size=random_size, replace=False)
        chunk = chunk.loc[random_indexes]
        data = pd.concat([data, chunk])
        del chunk
    
    return data
