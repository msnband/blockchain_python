
from block import Block
import datetime

block_chain = [Block.genesis_block()]
print("\nThe genesis block is created!")
print("Genesis Block Hash:", block_chain[-1].hash)

num_nodes_to_add = 6

for i in range(1, num_nodes_to_add+1):
    block_chain.append(Block(block_chain[-1].hash, "DATA!", datetime.datetime.now()))

    print(f"\n -Node #{i} hash --> {block_chain[i].hash}")