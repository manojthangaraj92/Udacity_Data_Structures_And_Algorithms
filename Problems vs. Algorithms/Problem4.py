# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 4: Dutch National Flag Problem

"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice,
that would still be an O(n) solution but it will not count as single traversal.
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_pos = 0
    two_pos = len(input_list) - 1

    current_index = 0
    while current_index <= two_pos:
        if input_list[current_index] == 0:
            input_list[current_index] = input_list[zero_pos]
            input_list[zero_pos] = 0
            zero_pos += 1
            current_index += 1
        elif input_list[current_index] == 2:
            input_list[current_index] = input_list[two_pos]
            input_list[two_pos] = 2
            two_pos -= 1
        else:
            current_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":

    #Test case 1
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    #Test case 2
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    #Test case 3
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    #Test case 4 Edge case
    test_function([0])
    # Test case 5 Edge case
    test_function([])