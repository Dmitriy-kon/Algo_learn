class DynamicArray:
    def __init__(self) -> None:
        self.values: list[int | None] = [None] * 8
        self.size = 8
        self.current_index = 0

    def add(self, value):
        self.values[self.current_index] = value
        self.current_index += 1

        if self.current_index == self.size:
            self.resize(self.size * 2)

    def pop(self):
        self.values[self.current_index] = None
        self.current_index -= 1

        if self.current_index < self.size // 4:
            self.resize(self.size // 2, True)

    def resize(self, new_size: int, decrease: bool = False) -> None:
        new_values = [None] * new_size
        size = self.size if not decrease else new_size

        for i in range(size):
            new_values[i] = self.values[i]

        self.values = new_values
        self.size = new_size


dyn_arr = DynamicArray()
for i in range(10):
    dyn_arr.add(i)
    print(dyn_arr.values, dyn_arr.size)

for i in range(7):
    dyn_arr.pop()
    print(dyn_arr.values, dyn_arr.size)
