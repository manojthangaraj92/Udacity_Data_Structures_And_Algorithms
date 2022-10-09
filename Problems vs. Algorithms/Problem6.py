# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 6: Max and Min in a Unsorted Array

"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time.
Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    minimum = ints[0]
    maximum = ints[0]
    for number in ints:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number

    return (minimum, maximum)


if __name__ == "__main__":
    ## Example Test Case of Ten Integers
    import random

    #Test case 1
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # Test case 2
    l = [random.randint(10,1000) for i in range(10)]
    random.shuffle(l)
    print("Pass" if (min(l),max(l)) == get_min_max(l) else "fail")

    # Test case 3 edge case
    l = [-25,-20,-15,-100,0,2,-999]
    print("Pass" if (min(l), max(l)) == get_min_max(l) else "fail")

    # Test case 4 edge case
    l = []
    output = None
    print("Pass" if output == get_min_max(l) else "Fail")

