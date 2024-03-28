class Queue:
    def __init__(self, max_size: int):
        self.head = 0
        self.tail = 0
        self.data = [None] * max_size

    def empty(self) -> bool:
        # Возвращает True, если очередь пуста
        return self.head == self.tail

    def push_back(self, x: int) -> None:
        # Проверяем, не переполнена ли очередь
        if (self.tail + 1) % len(self.data) == self.head:
            # Увеличиваем размер массива в два раза
            d = [None] * (len(self.data) * 2)
            pt = 0
            # Копируем элементы из старого массива в новый
            for i in range(self.head, len(self.data)):
                d[pt] = self.data[i]
                pt += 1
            for i in range(0, self.tail):
                d[pt] = self.data[i]
                pt += 1
            self.data = d
            self.head = 0
            self.tail = pt
        # Добавляем элемент в конец очереди
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % len(self.data)

    def pop_front(self) -> int:
        # Удаляем элемент из начала очереди
        if self.empty():
            return -1  # Возвращаем -1, если очередь пуста
        t = self.data[self.head]
        self.data[self.head] = None  # Очищаем место в массиве
        self.head = (self.head + 1) % len(self.data)
        return t

    def peek(self) -> int:
        # Возвращает элемент в начале очереди без его удаления
        if self.empty():
            return -1
        return self.data[self.head]
