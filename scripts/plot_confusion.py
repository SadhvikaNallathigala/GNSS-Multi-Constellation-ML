import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("../output/gnss_dataset.csv")

X = df[[
    "snr",
    "sv_num",
    "constellation",
    "sat_count",
    "mean_snr",
    "std_snr"
]]

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

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Clear Sky", "Metal Plate"]
)

disp.plot()

plt.savefig("../output/confusion_matrix.png")

plt.show()

print("Confusion matrix saved")