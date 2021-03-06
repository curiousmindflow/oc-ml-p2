#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dataframe_distribution_overview(data, figsize=(10, 3)):
    plt.figure(figsize=figsize)

    sns.barplot(x=data.columns, y=data.count())

    plt.title("Number of values per column", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.ylabel("Number values", size=16)
    plt.show()


def feature_distribution_univar(data, feature: str, feature_label: str, figsize=(10, 3)):
    plt.figure(figsize=figsize)

    if feature:
        sns.countplot(x=feature, data=data)
    else:
        sns.countplot(data=data)

    plt.title("Number of values per column", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.xlabel(feature_label, size=16)
    plt.ylabel("Number values", size=16)
    plt.show()


def feature_filling(data, feature, feature_label, figsize=(16, 4)):
    fig = plt.figure(figsize=figsize)
    fig.patch.set_facecolor("white")

    plt.pie(x=[data[feature].notna().sum(), data[feature].isna().sum()], labels=[feature_label, "N/A"], autopct='%.0f%%')

    plt.title("Fill percentage", size=20)
    plt.xticks(size=16)
    plt.yticks(size=16)
    plt.show()


def correlation_heatmap(data):
    plt.figure(figsize=(30, 20))

    correlation = data.corr()
    mask = np.triu(np.ones_like(correlation, dtype=bool))

    sns.heatmap(data=correlation, mask=mask, annot=True, vmax=.75, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.title("Correlation heatmap", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.show()


def feature_trend_bivar(data, feature1, feature1_label, feature2, feature2_label, divider=1):
    plt.figure(figsize=(20, 4))

    plt.title(f"{feature1_label} / {feature2_label} trend")

    sns.lineplot(y=data.loc[:, feature1].iloc[::divider], x=data.index[::divider], label=feature1_label)
    sns.lineplot(y=data.loc[:, feature2].iloc[::divider], x=data.index[::divider], label=feature2_label)


def feature_distribution_bivar(data, feature1, feature1_label, feature2, feature2_label, divider=1):
    plt.figure(figsize=(10, 6))

    sns.jointplot(x=feature1, y=feature2, data=data.iloc[::divider], kind="reg", color=None, joint_kws={"line_kws": {'color':'black'}})

    plt.title(f"{feature1_label} / {feature2_label} distribution", size=20)
    plt.xticks(size=16)
    plt.yticks(size=16)
    plt.xlabel(feature1_label, size=16)
    plt.ylabel(feature2_label, size=16)
    plt.show()


def feature_distribution_bivar_box(data, feature1: str, feature2: str, figsize=(10, 3)):
    plt.figure(figsize=figsize)

    sns.boxplot(x=feature1, y=feature2, data=data)

    plt.title(f"{feature1} / {feature2}", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.ylabel(f"{feature1}", size=16)
    plt.ylabel(f"{feature2}", size=16)
    plt.show()


# feautres: [
#  (feature_label_1, feature_data_1),
#  (feature_label_2, feature_data_2),
#   ...
# ]
def feature_distribution_multivar(features):
    plt.figure(figsize=(10, 3))

    mode_id = 0

    for f in features:
        sns.kdeplot(label=f[0], data=f[1], shade=True)
        id = modal_id(f[1])
        if id > mode_id:
            mode_id = id

    mode_name = modal_name(mode_id)

    plt.title(f"{mode_name} Distribution", size=20)
    plt.xticks(rotation=45, size=16, ha="right")
    plt.yticks(size=16)
    plt.ylabel("Occurences", size=16)
    plt.legend()
    plt.show()


def feature_distribution_univar_box(data, feature: str, figsize=(10, 3)):
    plt.figure(figsize=figsize)

    sns.boxplot(y=feature, data=data)

    plt.title(f"Distribution of {feature}", size=20)
    plt.xticks(size=16)
    plt.yticks(size=16)
    plt.xlabel(feature, size=16)
    plt.ylabel("Value", size=16)
    plt.show()


def modal_id(data):
    return len(data.mode())


def modal_name(id):
    if id == 0:
        return "No mode"
    elif id == 1:
        return "Uni-modal"
    elif id == 2:
        return "Bi-modal"
    else:
        return "Multi-modal"
