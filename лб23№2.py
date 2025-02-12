import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper

def example_function(n):
    total = sum(range(n))
    return total

example_function = measure_time(example_function)
example_function(1000000)
