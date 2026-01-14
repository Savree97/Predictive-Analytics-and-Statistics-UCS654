import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):

    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print("Error while reading input file:", e)
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns")
        sys.exit(1)

    try:
        matrix = data.iloc[:, 1:].astype(float).values
    except:
        print("Error: From 2nd column onward values must be numeric")
        sys.exit(1)

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
        print("Error: Number of weights, impacts and criteria must be same")
        sys.exit(1)

    for i in impacts:
        if i not in ["+", "-"]:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    normalized = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = distance_worst / (distance_best + distance_worst)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python 102317097.py <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
