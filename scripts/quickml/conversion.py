def feature_to_list(data, feature: str, delimiter=","):
    return data.apply(lambda x: cell_to_list(x, feature, delimiter), axis="columns")


def cell_to_list(row, feature: str, delimiter: str):
    if type(row[feature]) == str:
        row[feature] = row[feature].split(delimiter)
    else:
        row[feature] = []
    return row
