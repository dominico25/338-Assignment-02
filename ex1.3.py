# Function using memoization
def func(n, previous = {}):
    if n == 0 or n == 1:
        return n
    if n in previous:
        return previous[n]
    else:
        previous[n] = func(n-1, previous) + func(n-2, previous)
        return previous[n]




