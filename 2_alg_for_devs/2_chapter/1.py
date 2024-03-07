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


@timer
def binarry_search(arr: list, search: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == search:
            return mid
        if guess > search:
            right = mid - 1
        else:
            left = mid + 1
    return -1


@timer
def binarry_search2(arr: list, search: int):
    left = 0
    right = len(arr) - 1
    pos = len(arr) // 2

    while arr[pos] != search and left <= right:
        if search > arr[pos]:
            left += 1
        else:
            right -= 1
        pos = (left + right) // 2
    return -1 if left > right else pos


binarry_search2(arr, search)
binarry_search(arr, search)
print(arr[5])
