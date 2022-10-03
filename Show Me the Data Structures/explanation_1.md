## Course: Data Structures and Algorithms
## Project 2: Show Me the Data Structures
## Problem 1: LRU Cache

### Explanation of time and space complexity analysis
### Explanation
Python's dict is used as a cache, probably the best best data structure for mapping key to values and it has O(1) 
time complexity in average case.

### Time complexity
All operations has O(1) complexity and it is acheived with the help of double linked list to keep the order of the last recently used elements. 
It couldn't be single linked-list because in this case removing element in worst case take O(n).

### Space complexity
Space complexity is O(n) where n is number of elements in cache. 
We need to keep data about all elements.

