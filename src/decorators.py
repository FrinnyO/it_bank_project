from functools import wraps


def log(filename=""):
    """Декоратор, который логирует название функции и статус её"""

    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
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
