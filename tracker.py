class func_counter(object):
    def func_counter(self, func):
        def count(x):
            count.counter += 1
            return func(x)
        count.counter = 0
        return count