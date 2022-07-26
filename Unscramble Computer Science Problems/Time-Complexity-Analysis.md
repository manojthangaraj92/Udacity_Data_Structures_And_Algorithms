# Time Complexity Analysis for "Unscramble Computer Science Problems"

## TaskO:

In this task, the complexity of both subtasks are constant time i.e., O(1). This is because it gets executed only once to access the records.

## Task1:

In this task,
 - O(n) + O(n) : for the loop
 - O(n): for replacing the spaces

 Total time complexity = O(n+n+n) = O(n)

 ## Task2:

 In this task,

 - O(1) for empty dictionary
 - O(n) for looping through the calls
 - O(n) for getting the max time
 
 Total time complexity = O(1+n+n) = O(n)

 ## Task3:

 In this task,

 **PartA**

 - O(n) for finding the numbers which was called by (081)s.
 - O(1) for findind total called numbers in that month by (081)s
 - O(1) for empty list.
 - O(n) for looping through the calls list
 - O(n log n) for sorting
 - O(n) for the printing the codes.

 Time Complexity = O(n+1+1+n+ n*logn + n) = O(n log n)

 **PartB**

 O(1) for the code occurences initiation
 O(n) for the code occurences calculation
 O(1) for percentage calculation

 Time complexity = O(1+n+1) = O(n)

 ## Task4

 In this task, 
 - O(n) for creating outgoing calls
 - O(n) for creating outgoing texts
 - O(n) for creating incoming calls
 - O(n) for creating incoming texts
 - O(1) for creating the empty list
 - O(n) for looping through the outgoing calls list list
 - O(n log n) for sorting the my_list
 - O(n) for looping through the final telemarketing numbers.

 Total time complexity = O(n+n+n+1+n*log n+n) = O(n log n)