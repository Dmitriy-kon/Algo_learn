from functools import wraps
import random
import time

random.seed(1)
arr = random.sample(range(1, 10000), 1000)
arr.sort()

search = 8807


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter() - start

        name = func.__name__
        arg_str = ", ".join(f"{arg!r}" for arg in args)
        kwarg_str = ", ".join(
            f"{kwarg1!r} = {kwarg2!r}" for kwarg1, kwarg2 in kwargs.items()
        )
        print(f"[{end:.4f}s] {name}({arg_str}, {kwarg_str}) -> {res!r}")
        return res

    return wrapper


def remove_duplicates(array: list[int]):
    length = len(array)
    i = 0

    while i < length:
        found = False
        for k in range(i + 1, length):
            if array[k] == array[i]:
                found = True
                break

        if not found:
            i += 1
            continue

        for k in range(i + 1, length):
            array[k - 1] = array[k]
        length -= 1
    return length

if __name__ == '__main__':
    array = [15, 23, 20, 5, 15, 20, 15, 20, 44, 55]
    print("Original:", array)
    r = remove_duplicates(array)
    print("Unique:", array[:r])