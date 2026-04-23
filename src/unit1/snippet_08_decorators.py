def log_call(func):
    def wrapper(name):
        print(f"Calling {func.__name__} with argument: {name}")
        result = func(name)
        print(f"Result: {result}")
        return result
    return wrapper


@log_call
def greet(name):
    return f"Hello, {name}!"


print(greet("Ada"))

"""
Next:
* Create another decorator that measures the performance of the annotated function
"""