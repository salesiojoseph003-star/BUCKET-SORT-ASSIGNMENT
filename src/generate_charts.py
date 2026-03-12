import csv
import matplotlib.pyplot as plt

sizes = []
times = []

with open("results/experiment_results.csv") as file:

    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sizes.append(int(row[0]))
        times.append(float(row[1]))

plt.figure()

plt.plot(sizes, times, marker='o')

plt.title("Bucket Sort Runtime Performance")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")

plt.grid(True)

plt.savefig("results/charts/runtime_chart.png")

plt.show()