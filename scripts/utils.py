def fill_infos(df, col_name):
    total = df[col_name].count()
    nb_na = df[col_name].isna().sum()
    nb_fill = total - nb_na
    fill_percentage = total / (nb_na * 100)
    print(col_name + " total rows: ", total)
    print(col_name + " filled count: ", nb_fill)
    print(col_name + " filled percentage: ", fill_percentage)
