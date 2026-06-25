import matplotlib.pyplot as plt

models = ["RF", "SVM", "XGBoost", "LightGBM"]
accuracy = [100, 100, 100, 100]

plt.figure(figsize=(8,5))
plt.bar(models, accuracy)

plt.ylabel("Accuracy (%)")
plt.title("Model Comparison")

plt.savefig("../output/model_comparison.png")

plt.show()

print("Model comparison saved")