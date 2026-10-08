import pandas as pd


INPUT_FILE = "data/processed_crime.csv"


def analyze_crime_patterns():
    df = pd.read_csv(INPUT_FILE)

    print("\nNYC CRIME PATTERN ANALYSIS")
    print("==========================")

    print("\nTop 5 Boroughs by Crime Count")
    print("-----------------------------")
    print(df["boro_nm"].value_counts().head(5))

    print("\nTop 10 Crime Types")
    print("------------------")
    print(df["ofns_desc"].value_counts().head(10))

    print("\nCrime by Hour")
    print("-------------")
    print(df["hour"].value_counts().sort_index())

    print("\nCrime by Day of Week")
    print("--------------------")
    print(df["day_of_week"].value_counts())

    print("\nCrime by Law Category")
    print("---------------------")
    print(df["law_cat_cd"].value_counts())


if __name__ == "__main__":
    analyze_crime_patterns()