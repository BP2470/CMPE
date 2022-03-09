def doubler(func):
    def wrapper():
        print("One")
        func()
        print("Two")
        func()
    return wrapper
