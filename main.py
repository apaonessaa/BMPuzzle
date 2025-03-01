#!/usr/bin/python3
import sys
import random

from analyzer import Analyzer
from block import Block  

# Si vince la challenge, se seed=:flag e out.bmp sara' costruita a partire dalla sequenza win.
# La sequenza :win e' nota a priori, e si genera da :seed (PRG)
# Quindi, a partire da questa, definiamo una puzzle.bmp, in modo tale che: 
#   src.bmp = Union{ block[i]=puzzle[win[i]] } per i=0...n-1
# 
# Costruzione del puzzle
# Essendo la sol.bmp (original) caratterizzata dalla sequenza di blocchi ordinati: [0...i...n]
# Allora, block[i] = block_puzzle[ win[i] ] (!!!)
# Quindi, da win si costruisce puzzle come: puzzle[win[i]]=i.
# Es. Da seed="aaa", si ha:
#       win          allora si ha che:       puzzle
#       0: 3                                 1   :0     win[i]==0 => puzzle[0]=i
#       1: 0                                 4   :1
#       2: 4                                 3   :2
#       3: 2                                 0   :3
#       4: 1                                 2   :4   
def build_puzzle_seq(block: Block, win_seq):
    _, _, n = block.get_num()
    puzzle = [None] * n
    for i in range(n):
        puzzle[win_seq[i]] = i
    return puzzle

#
#
#
def apply(src: Analyzer, block: Block, seq):
    # Retrieve src image properties
    #width, height = src.get_size()
    rowsize = src.get_rowsize_Bpp()
    padding = src.get_padding()
    Bpp = src.get_Bpp()
    src_payload = src.get_payload()

    # Define output payload
    dst_payload = src_payload[:] # hard copy !!!

    # Retrive block properties
    b_width, b_heigth = block.get_properties()

    # seq[i] = j
    # src[iblock] => dst[jblock]
    for i in range(len(seq)):
        src_offset = block.get_offset(i)      
        dst_offset = block.get_offset(seq[i]) 

        for h in range(b_heigth):
            # copy entire block rowsize
            dst_payload[dst_offset : dst_offset + b_width*Bpp] = src_payload[src_offset : src_offset + b_width*Bpp]
            # next row
            src_offset += rowsize + padding
            dst_offset += rowsize + padding
    
    # apply
    src.set_payload(dst_payload)


if __name__ == "__main__":
    src = sys.argv[1]
    out = sys.argv[2]
    seed = sys.argv[3]
    opcode = sys.argv[4]

    b_width=250
    b_height=250

    random.seed(seed)

    # Require block size (b_width, b_height) must multiple of image (width, height)

    with open(src, "rb") as src:
        a1 = Analyzer(src.read())

    print()
    print("="*50)
    print(f"Puzzle {opcode}")
    print("-"*50)
    print(f"Image width, height: {a1.get_size()}")
    print(f"Pixel array size: {a1.get_payload_size()}")
    print(f"Bpp: {a1.get_Bpp()}")
    print(f"Seed: {seed}")
    print(f"Block width, height: {b_width}, {b_height}")
    print("="*50)
    print()

    # Build block
    block = Block(a1, b_width, b_height)

    _, _, n = block.get_num()
    sequence = random.sample(range(n),n)
    
    print("="*50)
    # Builder win seq
    if opcode == "generator":
        sequence = build_puzzle_seq(block, sequence)        
        print(f'Win sequence: {sequence}')
    elif opcode == "solver":
        print(f'Sequence: {sequence}')
    else:
        print("*"*20)
        print(f"Error with {opcode}.")
        print("*"*20)
        sys.exit(1)
    print("="*50+"\n")

    apply(a1, block, sequence)

    with open(out, "wb") as out:
        out.write(a1.raw_image)

    sys.exit(0)
