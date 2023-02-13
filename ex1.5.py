import matplotlib.pyplot as plt
import timeit

# List of numbers for 'n' from 0-35
time_list = [j for j in range(36)]

# Original
def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)

# Improved
def func2(n, previous = {}):
    if n == 0 or n == 1:
        return n
    if n in previous:
        return previous[n]
    else:
        previous[n] = func2(n-1, previous) + func2(n-2, previous)
        return previous[n]

# Timing results for original and improved each stored in a seperate list
original_elapsed_time = [(timeit.timeit(lambda : func1(i), number = i)) for i in time_list]
improved_elapsed_time = [(timeit.timeit(lambda : func2(i), number = i)) for i in time_list]
print(f'Elapsed time for original: {original_elapsed_time} seconds')
print(f'Elapsed time for improved version: {improved_elapsed_time} seconds')


# Plotting
plt.plot(time_list, original_elapsed_time, "b", label = "Original")
plt.plot(time_list, improved_elapsed_time, "g", label = "Improved")
plt.legend()
plt.xlabel("n")
plt.ylabel("Time")
plt.title("Timing Results based on n")
plt.show()
