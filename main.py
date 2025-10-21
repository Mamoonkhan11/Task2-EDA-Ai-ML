# Running EDA pipelines end to analyze datasets

import pandas as pd
from src.Eda_stats import save_summary_csv
from src.visuals import save_histogram, save_boxplot, save_pairplot, save_correlation_heatmap
from src.inference import basic_inferences

def run_eda():
    df = pd.read_csv("data/titanic.csv")
    print("Loaded:", df.shape)
    save_summary_csv(df, out_path="outputs/eda_summary.csv")
    print("Summary saved")
    save_histogram(df, "Age")
    save_histogram(df, "Fare")
    save_boxplot(df, "Fare")
    save_pairplot(df, ["Age","Fare","Pclass","SibSp"])
    save_correlation_heatmap(df)
    inferences = basic_inferences(df)
    print("Inferences:", inferences)

if __name__ == "__main__":
    run_eda()