## Course: Data Structures and Algorithms
## Problems Vs. Algoritms
## Problem 5: Autocomplete with Trie - Finding Suffixes

---
### Complexity Analysis

### TrieNode:
#### insert method

Time complexity of insert is the same as it's for set method for python dict. So in average case it's O(1), and 
O(n) in worst case.

Space complexity is constant O(1).

#### suffixes method

Time complexity is O(n), where n is number of children and children of sub_nodes of given node.

Space complexity in worst case is O(n), where n is number of children and children of sub_nodes of given node.
In the worst case all items we check turns out to be a suffix.

### Trie:
#### insert method

Time complexity in worst case is O(m * n), where m is number of chars in word and n is number of nodes in trie.
Space complexity is O(n).

#### find method

Time complexity in worst case is O(m * n), where m is number of chars in word and n is number of nodes in trie.
Space complexity is O(n)