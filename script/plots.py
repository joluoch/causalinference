import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns








def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()


def heat(data, color, size):
    
    corr = data.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(corr)] = True
    
    plt.figure(figsize=size)
    sns.heatmap(corr, mask=mask, annot=True, cmap=color)
    plt.show()


def pair_plot(data,hue: str):
    sns.pairplot(data, kind="scatter", hue=hue, plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.show()


def plot_box(df:pd.DataFrame, x_col:str, title:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()