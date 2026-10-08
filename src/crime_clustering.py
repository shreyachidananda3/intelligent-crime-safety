import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


INPUT_FILE = "data/processed_crime.csv"
OUTPUT_FILE = "data/crime_clusters.csv"


def create_crime_clusters():
    df = pd.read_csv(INPUT_FILE)

    features = df[
        ["latitude", "longitude", "hour"]
    ].copy()

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    df["crime_cluster"] = model.fit_predict(scaled_features)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nCRIME CLUSTERING RESULTS")
    print("========================")

    print(f"Total records analyzed: {len(df)}")
    print(f"Number of clusters: {df['crime_cluster'].nunique()}")

    print("\nRecords per cluster:")
    print(df["crime_cluster"].value_counts().sort_index())

    print("\nCluster characteristics:")
    print(
        df.groupby("crime_cluster")[
            ["latitude", "longitude", "hour"]
        ].mean().round(3)
    )

    print(f"\nSaved clustered dataset to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_crime_clusters()
