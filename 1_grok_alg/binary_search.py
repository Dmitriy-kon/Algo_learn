massive = list(range(0, 100, 4))

def binary_search(mas: list, item: int):
    low = 0
    hight = len(mas) - 1

    while low <= hight:
        mid = low + hight // 2

        guess = mas[mid]

        if guess == item:
            return mid
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1

print(binary_search(massive, 24))
