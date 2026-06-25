# scripts/plot_confusion_3class.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv("output/gnss_dataset_v2.csv")

X = df[
    [
        "snr",
        "sv_num",
        "constellation",
        "sat_count",
        "mean_snr",
        "std_snr"
    ]
]

X = pd.get_dummies(
    X,
    columns=["constellation"]
)

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

pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)

plt.figure(figsize=(8,6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="viridis",
    xticklabels=[
        "Clear Sky",
        "Metal Plate",
        "Foil"
    ],
    yticklabels=[
        "Clear Sky",
        "Metal Plate",
        "Foil"
    ]
)

plt.title("3-Class GNSS Environment Classification")
plt.xlabel("Predicted")
plt.ylabel("True")

plt.tight_layout()

plt.savefig(
    "output/confusion_matrix_3class.png",
    dpi=300
)

plt.show()