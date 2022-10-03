# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 3: Huffman Coding

# this code makes the tree that we'll traverse
from collections import Counter, OrderedDict

def set_frequency(input_str,reverse=False):
    if isinstance(input_str, str):
        countWord = Counter(input_str)
    return dict(sorted(countWord.items(), key=lambda x: x[1], reverse=reverse))

class Node(object):

    def __init__(self,char=None,freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def set_right_child(self, right):
        self.right = right

    def set_left_child(self, left):
        self.left = left

    def __repr__(self):
        string = f'Node:{self.char}, Frequency:{self.freq}, Left child:{self.left}, Right Child:{self.right}'
        return string

class NodeTree(object):
    def __init__(self,node):
        self.root = node

def huffman_encoding(data):

    wordCounter = set_frequency(data)

    nodes = []
    for key, value in wordCounter.items():
        nodes.append((key, value))
    tree = createTree(nodes)
    coding = encode(tree)
    #code_data
    return code_data(data,coding), tree

def createTree(nodeList):

    if len(nodeList) == 1:
        left = Node(char=nodeList[0][0], freq=None)
        root = Node(char=None, freq=nodeList[0][1])
        root.set_left_child(left)

        tree = NodeTree(root)
        return tree

    if len(nodeList) == 2:
        left = Node(char=nodeList[0][0], freq=None)
        right = Node(char=nodeList[1][0], freq=None)

        root = Node(char=None, freq=nodeList[0][1] + nodeList[1][1])
        root.set_left_child(left)
        root.set_right_child(right)

        tree = NodeTree(root)
        return tree

    last_element = nodeList[-1]
    rest_data = nodeList[:-1]

    tree = createTree(rest_data)

    left = Node(char=last_element[0], freq=None)
    new_root = Node(char=None, freq=tree.root.freq + last_element[1])
    new_root.set_left_child(left)
    new_root.set_right_child(tree.root)
    tree.root = new_root
    return tree

def encode(tree):
    root = tree.root
    if not root.left and not  root.right:
        return {root.freq: "0"}
    return encode_recursive(root, "")


def encode_recursive(root, current_code):
    if root is None:
        return {}

    codes = {}
    if root.char:
        codes[root.char] = current_code

    codes.update(encode_recursive(root.left, current_code + "0"))
    codes.update(encode_recursive(root.right, current_code + "1"))
    return codes

def code_data(data, codes):
    coding = ""
    for char in data:
        coding += codes[char]
    return coding


def huffman_decoding(data, tree):
    if not data:
        return ""

    decoded_string = ""
    node = tree.root
    for char in data:
        if char == "0":
            node = node.left
        else:
            node = node.right
        if not node.left and not node.right:
            decoded_string += node.char
            node = tree.root
    return decoded_string

if __name__ == "__main__":

    # Test Case 1
    x = huffman_encoding('AAABBBBBBCCCDDFFEEDDAAWW')
    print(x[0])
    y = huffman_decoding(x[0],x[1])
    print(y) #should reutrn the exact same letters

    # Test Case 2
    one_letter_sentence = huffman_encoding("AAAAAAAAAAA")
    print(one_letter_sentence[0])
    decode = huffman_decoding(one_letter_sentence[0], one_letter_sentence[1])
    print(decode)  # this should return the same AAAA... and all levels are as zero like a linked list

    # Test Case 3
    one_letter_sentence1 = huffman_encoding("B")
    print(one_letter_sentence1[0])
    decode1 = huffman_decoding(one_letter_sentence1[0], one_letter_sentence1[1])
    print(decode1) # This should decode justv a single value

    # Test Case 4
    one_letter_sentence1 = huffman_encoding(" ")
    print(one_letter_sentence1[0])
    decode1 = huffman_decoding(one_letter_sentence1[0], one_letter_sentence1[1])
    print(decode1) # This should a empty string




