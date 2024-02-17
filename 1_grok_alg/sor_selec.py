import timeit

def find_smallest(arr):
    smallest = arr[0]  # Хранение наименьшего значения
    smallest_index = 0  # Хранение индекса наименьшего значения

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

s = [6, 2, 1, 86, 123, 5234, -2, 12]



def find_smallest(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr




print('Time code 1', timeit.timeit("selection_sort(s)", setup="from __main__ import selection_sort, s", number=10))
print('Time code 2',timeit.timeit("find_smallest2(s)", setup="from __main__ import find_smallest2, s", number=10))
