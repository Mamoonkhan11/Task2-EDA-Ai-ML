# Saving plots and creting functions for visual analysis

import os
from unicodedata import numeric
import matplotlib.pyplot as plt
import seaborn as sns

def Save_histogram(df, column, out_dir="Outputs/visuals"):
    os.makedirs(out_dir, exist_ok=True)
    plt.figure(figsize=(8,4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f"Histogram: {column}")
    fname = f"{out_dir}/hist_{column}.png"
    plt.savefig(fname); plt.close()
    return fname

def Save_boxplot(df, column, out_dir="Outputs/visuals"):
    os.makedirs(out_dir, exist_ok=True)
    plt.figure(figsize=(8,4))
    sns.boxplot(x=df[column].dropna())
    plt.title(f"Boxplot: {column}")
    fname = f"{out_dir}/boxplot_{column}.png"
    plt.savefig(fname); plt.close()
    return fname

def Save_pairplot(df, cols, out_dir="outputs/visuals"):
    os.makedirs(out_dir, exist_ok=True)
    g = sns.pairplot(df[cols].dropna())
    fname = f"{out_dir}/pairplot.png"
    g.savefig(fname); plt.close()
    return fname

def Save_correlation_heatmap(df, out_dir="Outputs/visuals"):
    os.makedirs(out_dir, exist_ok=True)
    numeric_df = df.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    fname = f"{out_dir}/correlation_heatmap.png"
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(fname)
    plt.close()
    return fname