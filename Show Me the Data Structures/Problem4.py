# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 4: Active Directory

"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy
as such. Where User is represented by str representing their ids.
"""

class Group(object):
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for group in group.get_groups():
        return (is_user_in_group(user,group))
    return False

if __name__ == "__main__":

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    print(is_user_in_group(sub_child_user, sub_child))  # True

    # Test Case 2
    print(is_user_in_group("unknown user", sub_child))  # False

    # Test Case 3
    print(is_user_in_group(sub_child_user, parent))   # True

    # Test Case 4
    print(is_user_in_group(child, sub_child))  # False