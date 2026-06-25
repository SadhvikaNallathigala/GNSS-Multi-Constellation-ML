# sample_epochs.py

count = 0

with open("../data/sadhvika_01.26o","r",errors="ignore") as fin,\
     open("../data/sadhvika_01_sample.26o","w") as fout:

    header = True

    for line in fin:

        fout.write(line)

        if "END OF HEADER" in line:
            header = False
            continue

        if not header and line.startswith(">"):
            count += 1

        if count >= 1000:
            break

print("Created sample file")