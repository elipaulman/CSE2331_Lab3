# Elijah Paulman
# Timsort implementation
# Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort.

import time

def timsort(arr):
    # Define the minimum size of a run
    min_run = 64

    # Split the array into runs
    split_runs(arr, min_run)

    # Merge the runs
    merge_runs(arr, min_run)

def split_runs(arr, min_run):
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_runs(arr, min_run):
    n = len(arr)
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2

def merge(arr, start, mid, end):
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
arr = [5, 2, 8, 3, 1, 9, 4, 7, 6]
start_time = time.time()
timsort(arr)
end_time = time.time()

print("Sorted array:", arr)
print("Time taken:", end_time - start_time, "seconds")
