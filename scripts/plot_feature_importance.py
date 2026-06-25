import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("../output/gnss_dataset.csv")

features = [
    "snr",
    "sv_num",
    "constellation",
    "sat_count",
    "mean_snr",
    "std_snr"
]

X = df[features]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

importance = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.bar(features, importance)
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../output/feature_importance.png")

plt.show()

print("Feature importance saved")