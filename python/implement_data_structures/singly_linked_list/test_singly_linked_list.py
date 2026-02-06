import pytest

from singly_linked_list import LinkedList


def test_example_1():
    linked_list = LinkedList()

    linked_list.insertHead(1)
    linked_list.insertTail(2)
    linked_list.insertHead(0)

    assert linked_list.remove(1) is True
    assert linked_list.getValues() == [0, 2]


def test_example_2():
    linked_list = LinkedList()

    linked_list.insertHead(1)
    linked_list.insertHead(2)

    assert linked_list.get(5) == -1


def test_example_3():
    linked_list = LinkedList()

    linked_list.insertHead(1)

    assert linked_list.remove(0) is True


def test_example_4():
    linked_list = LinkedList()

    assert linked_list.get(0) == -1


def test_example_5():
    linked_list = LinkedList()

    linked_list.insertHead(1)

    assert linked_list.remove(2) is False
    assert linked_list.remove(1) is False


def test_example_6():
    linked_list = LinkedList()

    linked_list.insertHead(1)
    linked_list.insertHead(2)
    linked_list.insertTail(3)
    linked_list.insertTail(4)
    linked_list.insertHead(5)

    assert linked_list.get(0) == 5
    assert linked_list.get(2) == 1
    assert linked_list.get(4) == 4

    assert linked_list.remove(2) is True
    assert linked_list.remove(0) is True

    linked_list.insertHead(6)
    linked_list.insertTail(7)

    assert linked_list.getValues() == [6, 2, 3, 4, 7]
    assert linked_list.get(5) == -1
