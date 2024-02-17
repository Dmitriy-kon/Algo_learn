def _sum(arr):
    if arr == []:
        return 0
    return arr[0] + _sum(arr[1:])


def _len(arr):
    if arr == []:
        return 0
    return 1 + _len(arr[1:])


def _max(arr):
    if _len(arr) == 2:  # Т.к в конечном случае мы сравниваем 2 числа, то это и есть базовый случай
        return arr[0] if arr[0] > arr[1] else arr[1]
    submax= _max(arr[1:])
    return arr[0] if arr[0] > submax else submax


print(_sum(list(range(7))))
print(sum(list(range(7))))
print(_max(list(range(7))))
