with open("../data/sadhvika_01.26o", "r", errors="ignore") as f:

    for line in f:

        if "SYS / # / OBS TYPES" in line:
            print(line.strip())

        if "END OF HEADER" in line:
            break