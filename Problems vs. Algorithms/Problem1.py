# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 1: Finding the Square root of the integer.

"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1
    elif number == 1 or number == 1:
        return number
    else:
        end_number = number
        start_number = 0
        return recursive_sqrt(number, start_number, end_number)

def recursive_sqrt(number, start_num, end_num):
    mid_num = (start_num+end_num)//2
    if start_num > end_num:
        return mid_num
    if number == mid_num**2:
        return mid_num
    elif number <= mid_num**2:
        return recursive_sqrt(number,start_num,mid_num-1)
    else:
        return recursive_sqrt(number,mid_num+1,end_num)


if __name__ == "__main__":

    #Test case 1
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    # Test case 2 Edge case
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    # Test case 3
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")
    # Test case 4
    print("Pass" if (528 == sqrt(279345)) else "Fail")
    # Test case 5 Edge case
    print("Pass" if (-1 == sqrt(-1)) else "Fail")
    ## All test cases should pass
