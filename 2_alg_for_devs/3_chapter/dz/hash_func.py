class Student:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


def hash_string(value: str) -> int:
    res = 0
    for i in value:
        res += ord(i)
    return res


def hash_int(value: int) -> int:
    res = 1
    while value:
        last = value % 10
        res *= last
        value //= 10

    return res


def hash_student(value: Student) -> int:
    res = hash_int(value.age) + hash_string(value.name)
    return res


student1 = Student(21, "Alex")
stident2 = Student(34, "Andrey")
student3 = Student(21, "Alex")
print(hash_student(student1))
print(hash_student(stident2))
print(hash_student(student3))


# digit1 = 2731
# digit2 = 21312312
# digit3 = 2731
# print(hash_int(digit1))
# print(hash_int(digit2))
# print(hash_int(digit3))

# some_string1 = "teacher Alex"
# some_string2 = "Antoxa delogi"
# some_string3 = "teacher Alex"
# print(hash_string(some_string1))
# print(hash_string(some_string2))
# print(hash_string(some_string3))
