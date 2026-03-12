comparisons = 0
swaps = 0

def insertion_sort(arr):

    global comparisons, swaps

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0:

            comparisons += 1

            if arr[j] > key:
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        arr[j+1] = key

    return arr