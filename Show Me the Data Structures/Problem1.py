# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 1: LRU Cache

# important objective, All operations must take O(1) time.
#                       size of cache = 5

# create a class for double linked list node, double linked list node has the ability to link
# next node and previous which will help us do our operation in O(1) time.
class DoublyLinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# LRU cache class
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            raise ValueError("Only value greater than zero are allowed")

        self.capacity = capacity
        self.items = {}
        self.head = None
        self.tail = None
        self.size = 0

    # method to get the values
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.items:
            node = self.items[key]

            if node != self.head:
                self.delete(node)
                self.prepend(node)

            return node.value
            # if you get the value, then remove the value and put it at the top
        return -1

    # method to set the values
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.items:
            node = self.item[key]
            node.value = value

            if self.head != node:
                self.delete(node)
                self.prepend(node)
        else:
            new_node = DoublyLinkedListNode(key, value)
            if self.size == self.capacity:
                del self.items[self.tail.key]
                self.delete(self.tail)
                self.size -= 1
            self.prepend(new_node)
            self.items[key] = new_node
            self.size += 1

    # method to delete a node
    def delete(self, node):
        if self.capacity == 0:
            raise Exception('The dict is empty')

        if self.capacity == 1:
            self.head = None
            self.tail = None

        if self.tail == node:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = None
            node.prev = None
            node.next = None

        return node

    #method to prepend the node
    def prepend(self, node):

        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


if __name__ == "__main__":

    #case 1: This should raise an value Error
    try:
        our_cache = LRU_Cache(0)
    except:
        print("Pass, an Exception Occured")

    #case 2
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print("Pass" if (our_cache.get(1) == 1) else "Fail")
    print("Pass" if (our_cache.get(2) == 2) else "Fail")    # returns 1
    print("Pass" if (our_cache.get(3) == 3) else "Fail")   # returns 2
    print("Pass" if (our_cache.get(9) == -1) else "Fail")    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print("Pass" if (our_cache.get(4) == -1) else "Fail")

    our_cache.set(7, 7)

    print("Pass" if (our_cache.get(7) == 7) else "Fail")
    print("Pass" if (our_cache.get(1) == -1) else "Fail")

    #all test cases should pass