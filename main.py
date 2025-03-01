#!/usr/bin/python3
import sys
import random

from analyzer import Analyzer
from block import Block  

# The challenge is won if the seed is set to ':flag' and 'out.bmp' is built from the 'win' sequence.
# The ':win' sequence is predefined and generated from ':seed' (via a Pseudo-Random Generator - PRG).
# From this sequence, we define 'puzzle.bmp' such that:
#   src.bmp = Union{ block[i]=puzzle[win[i]] } for i=0...n-1
#
# **Building the puzzle sequence:**
# Given that the original 'sol.bmp' consists of ordered blocks [0...i...n], we construct 'puzzle' as follows:
# - Each block[i] in the source corresponds to block_puzzle[win[i]] in the puzzle.
# - The puzzle sequence is derived by reversing 'win', i.e., puzzle[win[i]] = i.
#
# Example: Given seed="aaa", we obtain:
#       win                      puzzle
#       0: 3          ->          1 : 0    # win[i]==0 => puzzle[0]=i
#       1: 0                      4 : 1
#       2: 4                      3 : 2
#       3: 2                      0 : 3
#       4: 1                      2 : 4

def build_puzzle_seq(block: Block, win_seq):
    _, _, n = block.get_num()
    puzzle = [None] * n  # Initialize puzzle sequence
    for i in range(n):
        puzzle[win_seq[i]] = i  # Reverse mapping of win sequence
    return puzzle


def apply(src: Analyzer, block: Block, seq):
    """
    Applies a transformation based on the sequence 'seq', rearranging blocks in the image.
    """
    # Retrieve image properties
    rowsize = src.get_rowsize_Bpp()
    padding = src.get_padding()
    Bpp = src.get_Bpp()
    src_payload = src.get_payload()

    # Create a copy of the original image payload
    dst_payload = src_payload[:]

    # Retrieve block properties
    b_width, b_heigth = block.get_properties()

    # Rearrange the blocks based on the given sequence
    for i in range(len(seq)):
        src_offset = block.get_offset(i)      # Get source block offset
        dst_offset = block.get_offset(seq[i]) # Get destination block offset

        for h in range(b_heigth):
            # Copy entire block row
            dst_payload[dst_offset : dst_offset + b_width * Bpp] = src_payload[src_offset : src_offset + b_width * Bpp]
            # Move to the next row
            src_offset += rowsize + padding
            dst_offset += rowsize + padding
    
    # Update the image with the transformed payload
    src.set_payload(dst_payload)


if __name__ == "__main__":
    # Parse command-line arguments
    src = sys.argv[1]   # Source image
    out = sys.argv[2]   # Output image
    seed = sys.argv[3]  # Seed for randomization
    opcode = sys.argv[4] # Operation mode: "generator" or "solver"

    # Define block size
    b_width = 250
    b_height = 250

    # Initialize random seed
    random.seed(seed)

    # Open and analyze the source image
    with open(src, "rb") as src:
        a1 = Analyzer(src.read())

    print("\n" + "=" * 50)
    print(f"Puzzle {opcode}")
    print("-" * 50)
    print(f"Image width, height: {a1.get_size()}")
    print(f"Pixel array size: {a1.get_payload_size()}")
    print(f"Bpp: {a1.get_Bpp()}")
    print(f"Seed: {seed}")
    print(f"Block width, height: {b_width}, {b_height}")
    print("=" * 50 + "\n")

    # Create block object
    block = Block(a1, b_width, b_height)

    # Generate a random sequence of block indices
    _, _, n = block.get_num()
    sequence = random.sample(range(n), n)
    
    print("=" * 50)
    
    # Determine operation mode
    if opcode == "generator":
        sequence = build_puzzle_seq(block, sequence)        
        print(f'Win sequence: {sequence}')
    elif opcode == "solver":
        print(f'Sequence: {sequence}')
    else:
        print("*" * 20)
        print(f"Error with {opcode}.")
        print("*" * 20)
        sys.exit(1)
    
    print("=" * 50 + "\n")
    
    # Apply transformation to the image
    apply(a1, block, sequence)

    # Save the transformed image
    with open(out, "wb") as out:
        out.write(a1.raw_image)

    sys.exit(0)