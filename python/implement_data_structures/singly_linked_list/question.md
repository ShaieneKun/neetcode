https://neetcode.io/problems/singlyLinkedList/question

Design a Singly Linked List class.

Your LinkedList class should support the following operations:

    LinkedList() will initialize an empty linked list.

    int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.

    void insertHead(int val) will insert a node with val at the head of the list.

    void insertTail(int val) will insert a node with val at the tail of the list.

    bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.

    int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

Example 1:

Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]

Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]

Example 3:

Input:
["insertHead", 1, "remove", 0]

Output:
[null, true]

Example 4:

Input:
["insertHead", 1, "remove", 2, "remove", 1]

Output:
[null, false, false]

Example 5:

Input:
["insertHead", 1, "insertHead", 2, "insertTail", 3, "insertTail", 4, "insertHead", 5, "get", 0, "get", 2, "get", 4, "remove", 2, "remove", 0, "insertHead", 6, "insertTail", 7, "getValues", "get", 5]

Output:
[null, null, null, null, null, 5, 1, 4, true, true, null, null, [6, 2, 3, 4, 7], -1]

Note:

    The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.

