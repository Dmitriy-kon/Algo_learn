from faker import Faker

fake = Faker()


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

        if self.number_of_element == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int, decrease: bool = False):
        new_entry = [None] * new_size
        size = self.size if not decrease else new_size

        for i in range(size):
            entry = self.entries[i]
            index = self.find_good_index(entry.key)

            new_entry[index] = entry

        self.entries = new_entry
        self.size = new_size

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

        for i in range(self.size):
            new_index = (index + i) % self.size

            entry = self.entries[new_index]
            
            if entry is None or entry.key == key:
                return new_index

        return -1


hs_map = HashMap()

for i in range(5):
    hs_map.add(str(i), fake.name())
    # print(hs_map.entries, hs_map.size)

print(hs_map.entries, hs_map.size)

for i in range(8):
    hs_map.add(str(i), fake.name())

print(hs_map.entries, hs_map.size)
hs_map.add(str(272), fake.name())
hs_map.add(str(272), fake.name())
    # print(hs_map.entries, hs_map.size)
print(hs_map.entries, hs_map.size)


for i in range(12):
    print(hs_map.get(str(i)))
