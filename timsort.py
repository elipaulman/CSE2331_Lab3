# Elijah Paulman
# Timsort implementation
# Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort.

import time
import random

def timsort(arr):
    # Define the minimum size of a run
    min_run = 64

    # Split the array into runs
    split_runs(arr, min_run)

    # Merge the runs
    merge_runs(arr, min_run)

def split_runs(arr, min_run):
    # Split the array into sorted runs of length min_run
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

def insertion_sort(arr, left, right):
    # Sort the elements in the range [left, right] using insertion sort
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_runs(arr, min_run):
    # Merge the sorted runs
    n = len(arr)
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2

def merge(arr, start, mid, end):
    # Merge two sorted subarrays [start, mid] and [mid+1, end]
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    left_len = mid - start + 1
    right_len = end - mid

    i = j = 0
    k = start

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < left_len:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < right_len:
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
arr = [random.randint(1, 1000) for _ in range(450)]
start_time = time.perf_counter()
timsort(arr)
end_time = time.perf_counter()

# Multiply by 1000 to convert seconds to milliseconds
time_taken = (end_time - start_time) * 1000

print("Sorted array:", arr)
print("Time taken: {:.6f} milliseconds".format(time_taken))