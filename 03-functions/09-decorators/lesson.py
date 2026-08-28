"""Lesson: decorators wrap a function to add behavior without rewriting it.

Objective: implement and use a basic decorator.
Mental model: a decorator is an adapter placed around a callable.
Real-world use: logging, timing, authentication, and caching.
"""

def announce_call(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@announce_call
def add(first, second):
    return first + second


add(2, 3)

# Active recall: why must wrapper return the original function's result?