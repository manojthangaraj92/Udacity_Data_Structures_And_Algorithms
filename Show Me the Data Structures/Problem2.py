# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 2: File Recursion

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == '':
        return []

    if not os.path.isdir(path):
        return None

    if len(os.listdir(path)) == 0:
        return []

    if os.path.isdir(path):
        DirList = os.listdir(path)

    file = [file for file in DirList if file.endswith('.'+suffix)]
    folders = [folder for folder in DirList if '.' not in folder]
    for folder in folders:
       file.extend(find_files(suffix=suffix, path=path+'/'+folder))
    return file

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
if __name__ == "__main__":
    # Test Case 1
    path = './testdir'
    pathFiles = find_files('c', path)
    print(pathFiles) #should return all c files in the directory

    # Test Case 2
    print(find_files("", ".")) #should return empty

    # Test Case 3
    print(find_files(".c", "")) #this should be none