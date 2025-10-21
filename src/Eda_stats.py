# Exporting and Computing Summary Statistics and Visualizations

import pandas as pd

def Compute_summary(df):
    desc = df.describe(include='all')
    skew = df.skew(numeric_only=True)
    missing = df.isnull().sum()
    summary = {
        'description': desc,
        'skewness': skew,
        'missing_values': missing
    }
    return summary

def Save_summary_csv(df, output_path='outputs/summary_statistics.csv'):
    desc = df.describe()
    desc.to_csv(output_path)
    return output_path
