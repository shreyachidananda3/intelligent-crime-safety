import pandas as pd
import matplotlib.pyplot as plt


INPUT_FILE = "data/processed_crime.csv"
OUTPUT_FILE = "screenshots/crime_by_borough.png"


def create_borough_chart():
    df = pd.read_csv(INPUT_FILE)

    borough_counts = (
        df["boro_nm"]
        .value_counts()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    borough_counts.plot(
        kind="bar"
    )

    plt.title("Reported Incidents in 100,000-Record NYC Sample by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of Reported Incidents")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)

    print(f"Chart saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_borough_chart()
