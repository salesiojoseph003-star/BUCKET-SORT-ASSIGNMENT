import random

def generate_dataset(size):
    """Generate a random dataset of the given size"""
    return [random.randint(0, 1000) for _ in range(size)]


# Chart generation code
import csv
import matplotlib.pyplot as plt

def generate_charts():
    sizes = []
    times = []
    comparisons = []
    swaps = []

    with open("results/experiment_results.csv") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:
            sizes.append(int(row[0]))
            times.append(float(row[1]))
            comparisons.append(int(row[2]))
            swaps.append(int(row[3]))

    # runtime chart
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time")
    plt.title("Bucket Sort Runtime")
    plt.grid(True)
    plt.savefig("results/charts/runtime_chart.png")

    # comparisons chart
    plt.figure()
    plt.plot(sizes, comparisons, marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Comparisons")
    plt.title("Comparisons vs Input Size")
    plt.grid(True)
    plt.savefig("results/charts/comparisons_chart.png")

    # swaps chart
    plt.figure()
    plt.plot(sizes, swaps, marker='o')
    plt.xlabel("Input Size")
    plt.ylabel("Swaps")
    plt.title("Swaps vs Input Size")
    plt.grid(True)
    plt.savefig("results/charts/swaps_chart.png")

if __name__ == "__main__":
    generate_charts()