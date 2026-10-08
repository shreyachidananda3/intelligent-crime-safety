import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier


INPUT_FILE = "data/processed_crime.csv"


def train_crime_model():
    df = pd.read_csv(INPUT_FILE)

    # Keep only records needed for prediction
    df = df[
        [
            "boro_nm",
            "hour",
            "month",
            "latitude",
            "longitude",
            "law_cat_cd"
        ]
    ].dropna()

    # Convert borough names into numeric values
    borough_encoder = LabelEncoder()
    df["boro_encoded"] = borough_encoder.fit_transform(
        df["boro_nm"]
    )

    # Convert target labels into numeric values
    target_encoder = LabelEncoder()
    df["target"] = target_encoder.fit_transform(
        df["law_cat_cd"]
    )

    features = [
        "boro_encoded",
        "hour",
        "month",
        "latitude",
        "longitude"
    ]

    X = df[features]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric="mlogloss"
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\nCRIME CATEGORY PREDICTION MODEL")
    print("===============================")

    print(f"Training records: {len(X_train)}")
    print(f"Testing records: {len(X_test)}")
    print(f"Model accuracy: {accuracy:.2f}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=target_encoder.classes_
        )
    )


if __name__ == "__main__":
    train_crime_model()
