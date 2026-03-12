from src.insertion_sort import insertion_sort, comparisons, swaps

def bucket_sort(arr):

    if len(arr) == 0:
        return arr

    bucket_count = 10

    max_val = max(arr)
    min_val = min(arr)

    bucket_range = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    sorted_list = []

    for bucket in buckets:
        sorted_bucket = insertion_sort(bucket)
        sorted_list.extend(sorted_bucket)

    return sorted_list