ages = [21, 19, 22, 19, 19, 20, 21, 25, 26, 24, 24, 25, 24]


def get_max_age(ages):
    max_age = float("-inf")
    
    for age in ages:
        if age > max_age:
            max_age = age
    return max_age

def get_min_age(ages):
    min_age = float("+inf")
    
    for age in ages:
        if age < min_age:
            min_age = age
    return min_age

def get_2_max_age(ages):
    max_age = float("-inf")
    second_max_age = float("-inf")
    
    for age in ages:
        if age > max_age:
            second_max_age = max_age
            max_age = age
            
    return max_age, second_max_age


def find_max_under_boundary(arr: list[int], top_boundary: int)  -> int:
    current_max = float("-inf")
    
    for i in range(len(arr)):
        if arr[i] < top_boundary:
            if arr[i] > current_max:
                current_max = arr[i]
    return current_max


def find_top_elements(arr: list[int], number_elem: int)  -> list[int]:
    top_elemets = []
    
    prev_max = float("inf")
    
    for _ in range(number_elem):
        current_max = find_max_under_boundary(arr, prev_max)
        prev_max = current_max
        top_elemets.append(current_max)
    return top_elemets

# print(get_max_age(ages))
# print(get_min_age(ages))
# print(get_2_max_age(ages))
print(find_top_elements(ages, 3))