import time
import subprocess
import random


def clock(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"[{end:.8f}s] {func.__name__} -> {res!r}")
        return res

    return wrapper


@clock
def get_divided_by_number(num: int) -> int:
    count = 0

    for i in range(100_000_000):
        if i % num == 0:
            count += 1
    return count


@clock
def get_odd_number_count(arr: list) -> int:
    count = 0
    for i in arr:
        if i % 2 == 1:
            count += 1
    return count


@clock
def get_prime_factors(n: int) -> list:
    count = 0
    res = []

    for i in range(2, n + 1):
        while n % i == 0:
            count += 1
            res.append(i)
            n //= i
    


    return res

@clock
def get_prime_factors2(n: int) -> list:
    res = []
    count = 0
    
    i = 2
    while i*i <=n:
        while n % i == 0:
            count += 1
            res.append(i)
            n //= i
        i += 1
    if n > 1:
        count += 1
        res.append(n)
    
    return res


def main():
    # subprocess.run("./1.exe")
    # print()
    # get_odd_number_count(arr)
    # get_divided_by_number(3)
    res2 = get_prime_factors2(1000)
    res = get_prime_factors(1000)
    # print(res)
    # print(res2)


if __name__ == "__main__":
    main()
