## Course: Data Structures and Algorithms
## Problems Vs. Algoritms
## Problem 7: Routing in a Web Server with a Trie

---
### RouteTrieNode:
#### insert method

Time complexity of insert is the same as it's for set method for python dict. 
So in average case it's O(1), and O(n) in worst case.

### Space complexity is constant O(1).

#### RootTrie:
#### Insert method

Time complexity in worst case is O(m * n), where m is number of parts in path and n is number of 
nodes in trie. Therefore its O(n)

Space complexity is O(1), I keep only info about current node, so space complexity is constant.

### Find method

Time complexity in worst case is O(m * n), where m is number of parts in path and 
n is number of nodes in trie. Therefore its O(n)

Space complexity is O(1), I keep only info about current node, so space complexity is constant.

### Router:
#### add_handler method

Here split_paths and insert from RootTrie is used. 
So it could be also summarized to O(m * n), where m is number of parts in path and n is number of nodes in trie.

#### lookup method

Here split_paths and find from RootTrie is used. 
So it could be summarized to O(m * n), where m is number of parts in path and n is number of nodes in trie

#### split_paths method

Time complexity is O(n), all elements must be checked to split string.
Space complexity is O(n) in worst case, for almost each element new list item will be created.