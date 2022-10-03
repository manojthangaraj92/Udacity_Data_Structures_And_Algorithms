## Course: Data Structures and Algorithms
## Project 2: Show Me the Data Structures
## Problem 4: Active Directory

### Explanation of time and space complexity analysis
### Explanation
To check if user is in group recursion is used, because to check if user is in given group we also need to check all groups below given. 
Users which is in child group also belong to parent group.

### Time complexity
All operations has O(n) where n is the number of groups and subgroups of a given group.

### Space complexity
Space complexity is O(n) in the worst case scenario where n is the number of groups and subgroups.