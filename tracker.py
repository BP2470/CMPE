def func_counter(func):
    def count(call):
        count.calls += 1
        return func(call)
    count.calls = 0
    return count