class DynamicArray:
    capacity = 0
    size = 0
    array = []

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None for i in range(capacity)]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if self.array[i] == None:
            self.size += 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        for i in range(self.getCapacity()):
            if self.array[i] == None:
                self.array[i] = n
                self.size += 1
                break

    def popback(self) -> int:
        size_minus_1 = self.getSize() - 1

        if size_minus_1 >= 0:
            index = size_minus_1
        else:
            index = 0

        last_element = self.array[index]
        self.array[index] = None

        self.size -= 1

        return last_element

    def resize(self) -> None:
        self.array += [None for i in range(self.getCapacity())]
        self.capacity = self.getCapacity() * 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
