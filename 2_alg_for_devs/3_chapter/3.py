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
        _hash = self.hash_func(key)
        index = _hash % self.size
        self.entries[index] = KeyValuePair(key, value)
        self.number_of_element += 1

        if self.number_of_element == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int, decrease: bool = False):
        new_entry = [None] * new_size
        size = self.size if not decrease else new_size

        for i in range(size):
            entry = self.entries[i]
            _hash = self.hash_func(entry.key)
            index = _hash % new_size
            
            new_entry[index] = entry

        self.entries = new_entry
        self.size = new_size

    def get(self, key: str):
        _hash = self.hash_func(key)
        index = _hash % self.size
        entry = self.entries[index]

        if entry is None:
            return None
        return self.entries[index]


hs_map = HashMap()

for i in range(10):
    hs_map.add(str(i), fake.name())
    print(hs_map.entries, hs_map.size)
print(hs_map.entries, hs_map.size)


for i in range(12):
    print(hs_map.get(str(i)))