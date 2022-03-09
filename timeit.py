import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print('Total time ' + str(end))
    return wrapper

