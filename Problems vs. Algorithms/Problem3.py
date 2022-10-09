# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 3: Rearrange Array Digits

"""
Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ
by more than 1. You're not allowed to use any sorting function that Python provides and the expected time
complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5].
The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list
    reverse_sorted = mergesort(input_list)

    first_element = ""
    for i in range(0,len(input_list),2):
        first_element += str(reverse_sorted[i])

    second_element = ""
    for i in range(1,len(input_list),2):
        second_element += str(reverse_sorted[i])
    return [int(first_element), int(second_element)]

def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left,right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged += right[right_index:]
    merged += left[left_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    #Test case 1
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test_function(test_case) # These test cases should pass

    #Test case 2 Edge case
    test_case = [[], []]
    test_function(test_case)  # These test cases should pass

    #Test case 3 Edge case
    test_case = [[0], [0]]
    test_function(test_case)  # These test cases should pass




