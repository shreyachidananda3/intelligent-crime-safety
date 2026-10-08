import pandas as pd
import matplotlib.pyplot as plt


INPUT_FILE = "data/crime_clusters.csv"
OUTPUT_FILE = "screenshots/crime_clusters.png"


def create_cluster_chart():
    df = pd.read_csv(INPUT_FILE)

    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(
        df["longitude"],
        df["latitude"],
        c=df["crime_cluster"],
        s=8,
        alpha=0.5
    )

    plt.title("NYC Crime Pattern Clusters")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.colorbar(scatter, label="Crime Cluster")

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)

    print(f"Chart saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_cluster_chart()