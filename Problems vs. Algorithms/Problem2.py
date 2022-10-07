# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 2: Search in an rotated array

"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) <= 0:
        return -1
    start_idx = 0
    end_idx = len(input_list) - 1
    return recursive_way(input_list, start_idx, end_idx, number)


def recursive_way(array, start_index, end_index, target):
    if start_index > end_index:
        return -1
    mid = (start_index + end_index) // 2

    if array[mid] == target:
        return mid
    if array[mid] >= array[start_index]:
        if target >= array[start_index] and target <= array[mid]:
            return recursive_way(array, start_index, mid - 1, target)
        else:
            return recursive_way(array, mid + 1, end_index, target)
    else:
        if target >= array[mid] and target <= array[end_index]:
            return recursive_way(array, mid + 1, end_index, target)
        else:
            return recursive_way(array, start_index, mid - 1, target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[-7, -6, -5, -4, -3, -2, -1, -10, -9, -8], -9])
    test_function([[], 20])

    ## All test cases should pass

