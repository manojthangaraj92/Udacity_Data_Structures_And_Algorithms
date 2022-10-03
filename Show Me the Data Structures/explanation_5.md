## Course: Data Structures and Algorithms
## Project 2: Show Me the Data Structures
## Problem 5: BlockChain

### Explanation of time and space complexity analysis
### Explanation
Three class methods is used to achieve this solution. A class Block
will have information about its hash key, previous hash key etc., 

The class BlockNode as node for this class block with the next method 
reference to the previous hash.

The class Blockchain as a kind of LinkedList method with head and previous 
methods to link different block nodes

### Time complexity
Adding an element has O(1) since it just adding the block nodes at the tail.
But the getting the block nodes has an O(n) time complexity as its 
traverse through the blockchain.

### Space complexity
Space complexity is O(n) for the blockchain where n is the number of elements added.