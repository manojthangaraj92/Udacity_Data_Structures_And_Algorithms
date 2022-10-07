## Course: Data Structures and Algorithms
## Problems Vs. Algoritms
## Problem 2: Rearrange Array Digits

---
### Solution

The task is to find the largest sum of two values derived the unsorted array.
It would be easy if the array is sorted in a reverse order and construct the two numbers
with an alternative indices.

Example:


Input: [1, 2, 3, 4, 5]


Sorted array from max to min numbers: [5, 4, 3, 2, 1]


x = 531


y = 42


Output: [531, 42]

### Time Complexity

The time complexity for this problem is O(nlog(n))
O(nlog(n)) -> for doing merge sort
O(n) -> for traversing through the sorted array

### Space 

The Space complexity is O(n) as number of spaces needed is depends on number of elements.