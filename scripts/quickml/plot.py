import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def feature_distribution(data, features):
    plt.figure(figsize=(10,3))

    barplot = sns.barplot(x=data, y=data[features].count())

    plt.title("Number of values per column", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.ylabel("Number values", size=16)
    plt.show()
