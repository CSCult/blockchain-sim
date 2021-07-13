"""
@Author: ADD YOUR NAME HERE
@Date Created: ADD DATE CREATED
@Title: BLOCKCHAIN SIMULATOR
"""

# Importing modules
import hashlib                 # hashlib for hashing algorithms
import datetime as date        # datetime for dates
import random                  # random for randomizing numbers for transactions 

class Block():
    """
        A certain block consists of the following entities:
        + Block height
        + Timestamp
        + Previous block hash
        + Transactions
        + Transactions counter
    """
    def __init__(self, height, timestamp, prev_hash, txs):
        pass

    #-------------------------------------------------------------------------------------

    """
    Generates hash using SHA-256 algorithm
    """
    def hashing(self, s):
        pass
    
    #-------------------------------------------------------------------------------------
    
    """
    Creates hash for the block
    """
    def hash_block(self):
        pass
    
    #-------------------------------------------------------------------------------------
    
    """
    Generates Merkle Root Hash for all transactions
    """
    def merkle_root_hash(self, txs):
        pass
    

"""
Creates the genesis block, i.e. the first block of the blockchain
"""
def create_genesis_block():
    # Manually construct a block with height zero and arbitrary previous hash
    pass


"""
Defines properties for the next block in the blockchain and returns Block object
"""
def next_block(last_block):
    pass


if __name__=="__main__":
    
    # Create blockchain as a list and add the genesis block

    # Let's add 20 blocks to the chain

    # We will be mining 20 blocks
    
        # Showing block information
    
    pass