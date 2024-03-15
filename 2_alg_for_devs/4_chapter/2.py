class DynoArray:
    def __init__(self) -> None:
        self.data = [None] * 1
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def set(self, inx: int, value: int):
        self.data[inx] = value

    def get(self, inx: int) -> int:
        return self.data[inx]

    def push(self, value: int) -> None:
        length = len(self.data)

        if self.length == length:
            data2 = [None] * (length * 2)

            for i in range(length):
                data2[i] = self.data[i]
                
            self.data = data2

        self.data[self.length] = value
        self.length += 1

    def pop(self) -> None:
        length = len(self.data)
        self.length -= 1
        
        if self.length < length // 4:
            data2 = [None] * (length // 2)

            for i in range(self.length):
                data2[i] = self.data[i]
            self.data = data2
    
    def insert(self, value: int, indx: int) -> None:
        self.push(0)
        for i in range(self.length - 1, indx, -1):
            self.data[i] = self.data[i - 1]
        self.data[indx] = value