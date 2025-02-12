import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = ', '.join(repr(a) for a in args)
        kwargs_repr = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        signature = ', '.join(filter(None, [args_repr, kwargs_repr]))
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

# Приклад використання
def example_usage():
    @trace
    def add(x, y):
        return x + y

    @trace
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    add(3, 5)
    greet("Alice")
    greet("Bob", greeting="Hi")

example_usage()