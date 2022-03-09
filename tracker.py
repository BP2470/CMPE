def func_counter(func):
    def count(x):
        count.counter += 1
        return func(x)
    count.counter = 0
    return count