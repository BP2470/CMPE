def func_counter(func):
    def wrapper(*args):
        wrapper.counter += 1
        return func(*args)
    wrapper.counter = 0
    return wrapper




"""class func_counter:
    def __init__(self, counter=0):
        self.counter = counter
    def __call__(self, func):
        def wrapper(*args):
            self.counter += 1
            return func(*args)
        return wrapper"""
