from datetime import time
from functools import wraps


def log(filename=""):
    """Декоратор, который логирует время начала и конца функции, а также её название"""
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(
                            f"""{func.__name__} start - {time_1}
{func.__name__} work
{func.__name__} stop - {time_2}
my_function ok"""
                        )
                else:
                    print(
                        f"""{func.__name__} start - {time_1}
{func.__name__} work
{func.__name__} stop - {time_2}
my_function ok"""
                    )
            except Exception as e:
                result = e
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. inputs: {args}, {kwargs}")
            return result

        return wrapper

    return timer
