## Course: Data Structures and Algorithms
## Project 2: Show Me the Data Structures
## Problem 3: Huffman Coding

### Explanation of time and space complexity analysis
### Explanation
In problem 3,class Node is used to keep information about 
charcters and their frequencies and also their left and right children nodes. 
Class NodeTree represents the huffman tree. To count frequencies of charts we used 
dict which is the best data structure to keep key - value mapping, 
which in this case are character - frequencies pairs.

### Time complexity
Time complexity is O(nlogn), iterating through the strings will be of O(n)
complexity and sorting is the most time-consuming operation in the encoding solution.

For decoding, the time complexity is O(n). It just iterate through the 
the tree.

### Space complexity
Space complexity is O(n) in both cases of encoding and decoding. In
the solution we iterate thought every element from decoded data 
and based on the value, going left or right on tree. There is no 
more iteration. 
