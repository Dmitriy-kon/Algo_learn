from functools import cache
import time
import sys

sys.setrecursionlimit(1000000)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"[{end:.8f}s] {func.__name__} -> {res!r}")
        return res

    return wrapper


def power_n(a: int, b: int):
    if b == 0:
        return 1
    return a * power_n(a, b - 1)


def power_log_n(a: int, b: int):
    if b == 0:
        return 1

    if b % 2 == 0:
        return power_log_n(a, b // 2) ** 2

        # spam = power_log_n(a, b // 2)
        # return spam * spam

    return a * power_log_n(a, b - 1)


@timer
def test_power_n():
    power_n(3, 500)


@timer
def test_power_log_n():
    power_log_n(3, 500)


if __name__ == "__main__":
    [i for i in range(500_0000)]
    [i for i in range(500_0000)]
    test_power_n()
    test_power_log_n()
