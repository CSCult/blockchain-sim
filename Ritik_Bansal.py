"""
@Author: Ritik Bansal
@Date Created: 28th of July 2021
@Title: BLOCKCHAIN SIMULATOR

"""

import hashlib                 # hashlib for hashing algorithms
from datetime import datetime        # datetime for dates
import random

class Block():
    def __init__(self,index, height, timestamp, prev_hash, txs, data):
        self.index = index
        self.height = height
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.txs = txs
        self.data = data
        self.hash = hash

MyBlockChain = []

def hashing(self, s):
    self.s =s
    self.hashValue = hashlib.sha256(value.encode('utf-8')).hexdigest()

def hash(self, string):
    string = string.encode()
    sha = hashlib.sha256(string).hexdigest()
    return sha

def merkle_root_hash(self, txs):
        if (len(txs) == 1):
            return txs[0]
        # New list for storing merkle root hashes
        newtxs = []
        for i in range(0, len(txs)-1, 2):
            newtxs.append(self.hashing(str(txs[i]) + str(txs[i+1])))
        if len(txs)%2 == 1:
            newtxs.append(self.hashing(str(txs[-1]) + str(txs[-1])))
        return self.merkle_root_hash(newtxs)

def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0", "txs")

MyBlockChain.append(create_genesis_block())


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "block no. {}".format(this_index)
    this_hash = last_block.hash

    return Block(this_index, this_timestamp, this_data,this_hash,)

for i in range(0,20):
    MyBlockChain.append(next_block(MyBlockChain[-1]))

for item in MyBlockChain:
    print(item.data)
