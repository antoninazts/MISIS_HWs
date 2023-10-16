def cash(func):
    fibonacci_cache = {}

    def wrapper(*args):
        if args in fibonacci_cache:
            return fibonacci_cache[args]

        result = func(*args)
        fibonacci_cache[args] = result
        return result

    return wrapper


@cash
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(8))