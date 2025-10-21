# Running EDA pipelines end to analyze datasets

import pandas as pd
from src.Eda_stats import Save_summary_csv
from src.visuals import Save_histogram, Save_boxplot, Save_pairplot, Save_correlation_heatmap
from src.inference import Basic_inference

def run_eda():
    df = pd.read_csv("Data/Titanic-Dataset.csv")
    print("Loaded:", df.shape)
    Save_summary_csv(df, output_path="Outputs/Eda_Summary.csv")
    print("Summary saved in Output Directory!")

    Save_histogram(df, "Age")
    Save_histogram(df, "Fare")
    Save_boxplot(df, "Fare")
    Save_pairplot(df, ["Age","Fare","Pclass","SibSp"])
    Save_correlation_heatmap(df)

    inferences = Basic_inference(df)
    def print_inferences(inferences):
        print("\n Basic Inferences \n")
        for title, info in inferences:
            print(f"# {title}:")
            if isinstance(info, dict):
                for key in sorted(info.keys()):
                    print(f"   {key}: {info[key]}")
            else:
                print(f"   {info}")
            print()

    print_inferences(inferences)

if __name__ == "__main__":
    run_eda()