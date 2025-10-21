# Basic Feature level inference functions for data preprocessing and feature extraction

import pandas as pd
import numpy as np

def basic_inference(df):
    inferences = []
    if 'Survived' in df.columns and 'Pclass' in df.columns:
        survival_rates = df.groupby('Pclass')['Survived'].mean()
        inferences.append((f"Survival rates by Pclass", survival_rates.to_dict()))

    skewness = df.skew(numeric_only=True.to_dict())
    inferences.append(("Skewness of numeric features", skewness))
    missing_values = df.isnull().sum().TO_dict()
    inferences.append(("Missing values per feature", missing_values))

    return inferences

                          