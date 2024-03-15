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

    def delete_element_at(self, index: int) -> None:
        self.values[index] = None
        self._shift_elements_left(index)
        self.current_index -= 1

        if self.current_index < self.size // 4:
            self.resize(self.size // 2, True)

    def insert(self, value: int, indx: int) -> None:
        self.add(0)
        self.current_index += 1

        if self.current_index == self.size:
            self.resize(self.size * 2)

        self._shift_elements_right(indx)
        self.values[indx] = value

    def resize(self, new_size: int, decrease: bool = False) -> None:
        new_values = [None] * new_size
        size = self.size if not decrease else new_size

        for i in range(size):
            new_values[i] = self.values[i]

        self.values = new_values
        self.size = new_size

    def _shift_elements_left(self, index: int) -> None:
        for i in range(index, self.current_index):
            self.values[i] = self.values[i + 1]

    def _shift_elements_right(self, index: int) -> None:
        for i in range(self.current_index, index, -1):
            self.values[i] = self.values[i - 1]


dyn_arr = DynamicArray()
for i in range(10):
    dyn_arr.add(i)
print(dyn_arr.values, dyn_arr.size)
print(dyn_arr.current_index)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
dyn_arr.delete_element_at(1)
print(dyn_arr.values, dyn_arr.size)
dyn_arr.add(100)
dyn_arr.add(100)
dyn_arr.add(100)
dyn_arr.add(100)
dyn_arr.add(100)
print(dyn_arr.values, dyn_arr.size)
print(dyn_arr.current_index)
dyn_arr.insert(200, 1)
dyn_arr.insert(200, 1)
dyn_arr.insert(200, 1)
dyn_arr.insert(200, 1)
dyn_arr.insert(200, 1)
print(dyn_arr.values, dyn_arr.size)

# for i in range(7):
#     dyn_arr.pop()
#     print(dyn_arr.values, dyn_arr.size)
