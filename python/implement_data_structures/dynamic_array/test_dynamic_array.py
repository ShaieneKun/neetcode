import pytest

from dynamic_array import DynamicArray


def test_example_1():
    arr = DynamicArray(1)
    assert arr.getSize() == 0
    assert arr.getCapacity() == 1


def test_example_2():
    arr = DynamicArray(1)
    arr.pushback(1)
    assert arr.getCapacity() == 1
    arr.pushback(2)
    assert arr.getCapacity() == 2


def test_example_3():
    arr = DynamicArray(1)

    outputs = []
    outputs.append(arr.getSize())
    outputs.append(arr.getCapacity())

    arr.pushback(1)
    outputs.append(arr.getSize())
    outputs.append(arr.getCapacity())

    arr.pushback(2)
    outputs.append(arr.getSize())
    outputs.append(arr.getCapacity())

    outputs.append(arr.get(1))

    arr.set(1, 3)
    outputs.append(arr.get(1))

    outputs.append(arr.popback())
    outputs.append(arr.getSize())
    outputs.append(arr.getCapacity())

    assert outputs == [0, 1, 1, 1, 2, 2, 2, 3, 3, 1, 2]
