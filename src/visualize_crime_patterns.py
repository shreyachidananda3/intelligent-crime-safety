import pandas as pd
import matplotlib.pyplot as plt


INPUT_FILE = "data/processed_crime.csv"
OUTPUT_FILE = "screenshots/crime_by_hour.png"


def create_hourly_chart():
    df = pd.read_csv(INPUT_FILE)

    hourly_counts = df["hour"].value_counts().sort_index()

    plt.figure(figsize=(10, 6))

    plt.plot(
        hourly_counts.index,
        hourly_counts.values,
        marker="o"
    )

    plt.title("NYC Crime Reports by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Reported Incidents")
    plt.xticks(range(24))
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)

    print(f"Chart saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_hourly_chart()