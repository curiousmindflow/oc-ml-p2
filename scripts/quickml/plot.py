import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def feature_distribution(data, features):
    plt.figure(figsize=(10,3))

    sns.barplot(x=data, y=data[features].count())

    plt.title("Number of values per column", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.ylabel("Number values", size=16)
    plt.show()


def feature_filling(x, labels):
    fig = plt.figure(figsize=(16,4))
    fig.patch.set_facecolor("white")

    plt.pie(x=x, labels=labels, autopct='%.0f%%')

    plt.title("Fill percentage", size=20)
    plt.xticks(size=16)
    plt.yticks(size=16)
    plt.show()

def correlation_heatmap(correlation):
    plt.figure(figsize=(30, 20))

    mask = np.triu(np.ones_like(correlation, dtype=bool))

    sns.heatmap(data=correlation, mask=mask, annot=True, vmax=.75, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.title("Correlation heatmap", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.show()

def feature_trend_bivar():
    pass