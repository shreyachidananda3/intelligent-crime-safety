import pandas as pd


INPUT_FILE = "data/processed_crime.csv"


def generate_recommendation(borough, hour):
    df = pd.read_csv(INPUT_FILE)

    borough_data = df[
        df["boro_nm"].str.upper() == borough.upper()
    ]

    if borough_data.empty:
        print(f"No data found for borough: {borough}")
        return

    nearby_hours = [
        hour,
        (hour - 1) % 24,
        (hour + 1) % 24
    ]

    time_data = borough_data[
        borough_data["hour"].isin(nearby_hours)
    ]

    total_crimes = len(borough_data)
    nearby_crimes = len(time_data)

    top_crimes = (
        time_data["ofns_desc"]
        .value_counts()
        .head(5)
    )

    print("\nSAFETY INSIGHT")
    print("==============")

    print(f"Borough: {borough.upper()}")
    print(f"Requested hour: {hour}:00")
    print(f"Total records for borough: {total_crimes}")
    print(f"Records around requested time: {nearby_crimes}")

    print("\nMost Common Crime Types Around This Time:")

    for crime, count in top_crimes.items():
        print(f"- {crime}: {count}")

    if nearby_crimes > 0:
        activity_ratio = nearby_crimes / total_crimes

        if activity_ratio >= 0.06:
            insight = "Higher reported crime activity in this sample."
        elif activity_ratio >= 0.03:
            insight = "Moderate reported crime activity in this sample."
        else:
            insight = "Lower reported crime activity in this sample."

        print("\nData-Driven Insight:")
        print(insight)

    print(
        "\nNote: This is a data-based pattern insight, "
        "not a guarantee of safety."
    )


if __name__ == "__main__":
    generate_recommendation("Brooklyn", 18)