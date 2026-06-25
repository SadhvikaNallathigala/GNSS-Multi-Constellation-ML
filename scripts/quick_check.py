# quick_check.py

with open("../data/sadhvika_01.26o", "r", errors="ignore") as f:

    count = 0

    for line in f:

        if line.startswith(">"):
            count += 1

    print("Epochs:", count)