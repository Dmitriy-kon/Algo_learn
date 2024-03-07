from faker import Faker

fake = Faker()

phone_numbers = [
    "187773456201",
    "187773456201",
    "87776543820",
    "87779876543",
    "287771234567",
    "87775678901",
    "87772345678",
    "87774567890",
    "87778765432",
    "87770123456",
    "87778901234",
    "287771234567",
]

balances = [392, 184, 217, 289, 356, 402, 168, 231, 305, 274, 392, 289]


class KeyValuePair:
    def __init__(self, key: str = None, value: str = None) -> None:
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"({self.key}, {self.value})"


class HashMap:
    def __init__(self) -> None:
        self.entries: list[KeyValuePair | None] = [None] * 8
        self.size = 8
        self.number_of_element = 0

    def hash_func(self, key: str):
        return 0 + int(key)

    def add(self, key: str, value: str):
        index = self.find_good_index(key)
        if self.entries[index] is None:
            self.number_of_element += 1

        self.entries[index] = KeyValuePair(key, value)

        if self.number_of_element > self.size * 0.7:
            self.resize(self.size * 2)

    def resize(self, new_size: int, decrease: bool = False):
        old_entries = self.entries
        self.entries = [None] * new_size
        self.size = new_size
        self.number_of_element = 0

        for i in range(len(old_entries)):
            entry = old_entries[i]
            if entry is not None:
                self.add(entry.key, entry.value)

    def get(self, key: str):
        index = self.find_good_index(key)
        if index == -1:
            return None
        entry = self.entries[index]

        if entry is None:
            return None
        return entry

    def find_good_index(self, key: str):
        _hash = self.hash_func(key)
        index = _hash % self.size
        start_index = index

        while True:
            entry = self.entries[index]
            if entry is None or entry.key == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                return -1

    def get_unique_numbers(self, input_array: list[int]) -> list[int]:
        unique_numbers = []
        for number in input_array:
            if self.get(number) is None:
                self.add(number, "exist")
                unique_numbers.append(number)
        return unique_numbers

    def delete_key(self, key: str):
        index = self.find_good_index(key)
        if index != -1 and self.entries[index] is not None:
            self.entries[index] = None
            self.number_of_element -= 1

    def get_all_keys(self):
        return [i.key for i in self.entries if i]

    def get_all_values(self):
        keys = self.get_all_keys()
        res = []
        for i in keys:
            entrie = self.get(i)
            if entrie:
                res.append(entrie.value)
        return res


hs_map = HashMap()

# for i in range(len(phone_numbers)):
#     if phone_numbers[i] == "87778901234":
#         print("THIS IS '87778901234'", balances[i])

#     hs_map.add(phone_numbers[i], balances[i])

# print(hs_map.get("87778901234"))

# print(hs_map.get_all_keys())
# print(hs_map.get_all_values())
# print(hs_map.number_of_element)

# print(len(hs_map.get_all_keys()))
# print(len(hs_map.get_all_values()))
# print(hs_map.entries, hs_map.size)
# print(hs_map.get("87776543820"))

# print(hs_map.entries)
# hs_map.delete_key("87776543820")
# print(hs_map.get("87776543820"))
# print(hs_map.entries)
# print(len(phone_numbers))

res = hs_map.get_unique_numbers(phone_numbers)
print(sorted(hs_map.get_all_keys()))
print(sorted(res))


# def are_there_two_numbers(numbers: list[int], x: int) -> bool:
#     num_dict = {}
#     for num in numbers:
#         if x - num in num_dict:
#             return num, num_dict[x - num]
#         num_dict[num] = num
#     return False

# print(are_there_two_numbers(numbers, find_sum))
