def func_counter(func):
    counter += 1

@func_counter
def tracker(func):
    func()

print('Times called: ' + tracker.counter)   
