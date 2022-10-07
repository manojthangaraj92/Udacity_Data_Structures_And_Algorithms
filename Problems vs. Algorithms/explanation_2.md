## Course: Data Structures and Algorithms
## Problems Vs. Algoritms
## Problem 2: Search in an rotated array

---
### Solution

- This problem is solved using the recursive binary search approach where the base cases are 

Base Case -> mid of array == target, return mid of array
Otherwise, check if left part is constantly increasing, if so, 
if the target is greater and lesser than start and mid respectively, do a recursive search
otherwise do a recursive search from mid to end

Another condition is, if left part is constant decreasing , if target is greater than mid
and lesser than end index, do a recursive search there, otherwise do a recursive search from start to mid
as rotated sorted array, possibilities are to be in other end.

### Time Complexity

The time complexity for this problem is O(log(n)) as this was the recursive binary search

### Space 

The Space complexity is O(1) as algorithm takes no extra space.