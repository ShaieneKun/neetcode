from typing import List

class LinkedList:

    array: List[int] = []

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        len_arr = len(self.array)
        index_gt_len_arr_minus_1 = index > len(self.array) - 1
        if (index < 0
            or index_gt_len_arr_minus_1
            or len_arr == 0):
            return -1
        return self.array[index]


    def insertHead(self, val: int) -> None:
        self.array = [val] + self.array

    def insertTail(self, val: int) -> None:
        self.array = self.array + [val]

    def remove(self, index: int) -> bool:
        len_arr = len(self.array)
        index_lt_0 = index < 0
        index_gte_0_len_arr = index >= len_arr

        if (index_lt_0
            or index_gte_0_len_arr
            or len_arr == 0):

            return False

        self.array = self.array[:(index)] + self.array[(index + 1):]
        return True

    def getValues(self) -> List[int]:
        return self.array
