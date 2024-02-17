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

print(get_max_age(ages))
print(get_min_age(ages))