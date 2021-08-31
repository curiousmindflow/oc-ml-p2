def index_lth(pd, np, df, percentage: int):
    percentage = percentage / 100
    less_than = df.count() < df.shape[0] * percentage
    index_less_than = less_than[less_than == True].index
    return index_less_than
