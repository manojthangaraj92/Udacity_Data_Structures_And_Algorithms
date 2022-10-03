# Course: Data Structures and Algorithms
# Project 2: Show Me the Data Structures
# Problem 5: BlockChain

import hashlib
import datetime

class Block:

    def __init__(self, data, previous_hash=None):
        self.data = data
        self.prev_hash = previous_hash
        self.timestamp = self.get_time()
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        if self.data !="" and isinstance(data,str):
            hash_str = self.data.encode('utf-8')
            sha.update(hash_str)
            return sha.hexdigest()
        return None

    def get_time(self):
        return datetime.datetime.now()

    def __repr__(self):
        if self.hash is None:
            emptystring = f'Hash:{self.hash}'
            emptystring += f'\nPlease enter a valid characters'
            return emptystring
        string = f'Data:{self.data}'
        string += f'\nHash:{self.hash}'
        string += f'\nPrevious Hash:{self.prev_hash}'
        string += f'\nTimestamp:{self.timestamp}'
        return string

class BlockNode:

    def __init__(self, data, prev_hash):
        self.data = Block(data, prev_hash)
        self.next = None

class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            prev_hash = 0
            self.head = BlockNode(data, prev_hash)
            self.tail = self.head
            return
        else:
            prev_hash = self.tail.data.hash
            self.tail.next = BlockNode(data, prev_hash)
            self.tail = self.tail.next
            self.tail.prev_hash = prev_hash
            return

    def get_block_nodes(self):
        if self.head is not None:
            currentBlock = self.head
            out_string = ''
            while currentBlock:
                block = currentBlock.data
                out_string += f'\n{block}'
                currentBlock = currentBlock.next
            return out_string
        return None

if __name__ == "__main__":

    # Test case 1
    data = 'Hello Block'
    block = Block(data, 0)
    print(block)    #just return the single block with its hash

    # Test case 2
    blockchain = BlockChain()
    blockchain.append("Apple")
    blockchain.append("Orange")
    blockchain.append("Banana")
    blockchain.append("Strawberry")
    blockchain.append("Blueberry")
    blockchain.append("Apricot")
    blockchain.append("Rasberry")

    print(blockchain.get_block_nodes()) #should return all the elements appended

    # Test case 3
    blockchain = BlockChain()
    blockchain.append("")
    print(blockchain.get_block_nodes()) #should return None hash

