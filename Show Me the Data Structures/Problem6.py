# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 6: Union and Intersection
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def to_set(self):
        outSet = set()
        if self.head is not None:
            currentNode = self.head
            while currentNode:
                outSet.add(currentNode.value)
                currentNode = currentNode.next

            return outSet
        return None

def union(llist_1, llist_2):
    # Your Solution Here
    assert isinstance(llist_1, type(LinkedList()))
    assert isinstance(llist_2, type(LinkedList()))

    set_llist1 = llist_1.to_set()
    set_llist2 = llist_2.to_set()

    out_llist = LinkedList()
    if llist_1.size() >= 1 and llist_2.size() >= 1:
        for item in set_llist1:
            set_llist2.add(item)
        for item in set_llist2:
            out_llist.append(item)
        return out_llist
    elif llist_1.size() == 0 and llist_2.size() >= 1:
        for item in set_llist2:
            out_llist.append(item)
        return out_llist
    elif llist_1.size() == 1 and llist_2.size() >= 0:
        for item in set_llist1:
            out_llist.append(item)
        return out_llist
    else:
        return out_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    assert isinstance(llist_1, type(LinkedList()))
    assert isinstance(llist_2, type(LinkedList()))

    list1 = llist_1.to_set()
    list2 = llist_2.to_set()

    outList = LinkedList()
    if llist_1.size() >= 1 and llist_2.size() >= 1:
        for item in list1:
            if item in list2:
                outList.append(item)
        if outList.size() == 0:
            string = "Intersection is empty"
            return string
        return outList


if __name__ == "__main__":

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [random.randint(1,100) for i in range(10)]
    element_2 = [random.randint(1,100) for i in range(10)]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union")
    print(union(linked_list_1, linked_list_2))
    print("Intersection")
    print(intersection(linked_list_1, linked_list_2)) #THE SHOULD BE AN NUMBER IF RANDOM GENERATED NUMBERS ARE EQUAL

    # Test case 2
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [i for i in range(1,10)]
    element_2 = [i for i in range(1,10,2)]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union")
    print(union(linked_list_1, linked_list_2))
    print("Intersection")
    print(intersection(linked_list_1, linked_list_2)) #only the odd number should be on intersection

    # Test case 3
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [random.randint(1, 100) for i in range(10)]
    element_2 = [random.randint(101, 200) for i in range(10)]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union")
    print(union(linked_list_1, linked_list_2))
    print("Intersection")
    print(intersection(linked_list_1, linked_list_2)) #there should not be any intersection




