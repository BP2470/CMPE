def doubler(func):
    def wrapper():
        func()
    return wrapper
