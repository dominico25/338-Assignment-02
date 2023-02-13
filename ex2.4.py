import sys
import json
import timeit
import matplotlib.pyplot as plt

# Modified code to improve performance by having pivot not initially at the start of the list
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        arr[low], arr[mid] = arr[mid], arr[low]
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Reading json file into initial_array
with open("ex2.json", "r") as file:
        initial_array = json.load(file)

# Timing for function
elapsed_time = [(timeit.timeit(lambda : func1(initial_array[i], 0, len(initial_array[i])-1), number = len(initial_array))) for i in range(len(initial_array))]

# List of array sizes
array_sizes = [len(initial_array[n]) for n in range(len(initial_array))]

# Plotting
plt.plot(array_sizes, elapsed_time)
plt.title("Elapsed Time vs Size of Array")
plt.xlabel("Size of Array")
plt.ylabel("Elapsed Time")
plt.show()



