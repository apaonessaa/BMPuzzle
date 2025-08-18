#!/usr/bin/python3
from enum import Enum
import random

from src.analyzer import Analyzer
from src.block import Block

class Mode(Enum): GENERATOR=1; SOLVER=2; 

class Puzzle():
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

    def __init__(self, src: str, b_width: int, b_height: int, debug: bool=False):
        # Open and analyze the source image
        with open(src, "rb") as src:
            self.analyzer = Analyzer(src.read())
        # Create block object
        self.block = Block(self.analyzer, b_width, b_height)
        self.debug = debug

        
    def build_puzzle_seq(self, block: Block, win_seq):
        _, _, n = block.get_num()
        puzzle = [None] * n  # Initialize puzzle sequence
        for i in range(n):
            puzzle[win_seq[i]] = i  # Reverse mapping of win sequence
        return puzzle


    def shuffle(self, src: Analyzer, block: Block, seq):
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

    def run(self, mode: Mode, out: str, secret):
        # Generate a random sequence of block indices
        _, _, n = self.block.get_num()
        # Build the sequence
        random.seed(secret)
        sequence = random.sample(range(n), n)  
        if mode == Mode.GENERATOR:
            sequence = self.build_puzzle_seq(self.block, sequence)                  
        # Apply transformation to the image
        self.shuffle(self.analyzer, self.block, sequence)
        # Save the transformed image
        with open(out, "wb") as out:
            out.write(self.analyzer.raw_image)
        return 0

    """
    def debug():
        print("\n" + "=" * 50)
        print(f"Puzzle Generation")
        print("-" * 50)
        print(f"Image width, height: {a1.get_size()}")
        print(f"Pixel array size: {a1.get_payload_size()}")
        print(f"Bpp: {a1.get_Bpp()}")
        print(f"Seed: {seed}")
        print(f"Block width, height: {b_width}, {b_height}")
        print("=" * 50 + "\n")

        print("=" * 50)
        print(f'Win sequence: {sequence}')
        print("=" * 50 + "\n")
    """
