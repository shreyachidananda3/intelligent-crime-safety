import pandas as pd


INPUT_FILE = "data/nyc_crime.csv"
OUTPUT_FILE = "data/processed_crime.csv"


def load_and_clean_data():
    print("Loading NYC crime dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Original records: {len(df)}")

    # Select the columns needed for our analysis
    columns = [
        "cmplnt_num",
        "boro_nm",
        "cmplnt_fr_dt",
        "cmplnt_fr_tm",
        "law_cat_cd",
        "ofns_desc",
        "prem_typ_desc",
        "addr_pct_cd",
        "latitude",
        "longitude"
    ]

    df = df[columns].copy()

    # Convert date and time fields
    df["crime_date"] = pd.to_datetime(
        df["cmplnt_fr_dt"],
        errors="coerce"
    )

    df["crime_time"] = pd.to_datetime(
        df["cmplnt_fr_tm"],
        format="%H:%M:%S",
        errors="coerce"
    )

    # Create useful time-based features
    df["year"] = df["crime_date"].dt.year
    df["month"] = df["crime_date"].dt.month
    df["day_of_week"] = df["crime_date"].dt.day_name()
    df["hour"] = df["crime_time"].dt.hour

    # Remove records missing important information
    df = df.dropna(
        subset=[
            "boro_nm",
            "ofns_desc",
            "law_cat_cd",
            "latitude",
            "longitude"
        ]
    )

    # Remove invalid geographic coordinates
    df = df[
        (df["latitude"].between(40.4, 40.95))
        & (df["longitude"].between(-74.3, -73.6))
    ]

    # Save cleaned dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Cleaned records: {len(df)}")
    print(f"Saved cleaned dataset to: {OUTPUT_FILE}")

    return df


if __name__ == "__main__":
    load_and_clean_data()