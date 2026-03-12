import time
import csv

from data.dataset_generator import generate_dataset
from src.bucket_sort import bucket_sort
import src.insertion_sort as counter

sizes = [1,2,3,4,5,10,250,999,9999,89786,789300,1780000]

def run_experiments():

    with open("results/experiment_results.csv","w",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Size","Time","Comparisons","Swaps"])

        for size in sizes:

            print("Running test for size:", size)

            data = generate_dataset(size)

            counter.comparisons = 0
            counter.swaps = 0

            start = time.time()

            bucket_sort(data)

            end = time.time()

            runtime = end - start

            writer.writerow([
                size,
                runtime,
                counter.comparisons,
                counter.swaps
            ])

            print("Time:", runtime)
            print("Comparisons:", counter.comparisons)
            print("Swaps:", counter.swaps)
            print("---------------------")