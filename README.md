# BMPuzzle

**BMPuzzle** is a command-line tool that transforms BMP images into puzzles and allows you to solve them. 

The core idea is to split the image into blocks, shuffle them according to a sequence generated from a **secret**, and then use the same secret to reconstruct the original image.

<p align="center">
  <img width="640" height="214" alt="puzzle" src="https://github.com/user-attachments/assets/a5cb54e8-b783-4177-8150-606861fd46b4" />
</p>

### How it works

1. The image is divided into square blocks.
2. The blocks are shuffled following an order derived from a secret (a key/seed).
3. To rebuild the image, you need to provide the same secret: this ensures that the blocks are placed back in their original position.

### Block size selection

The block size cannot be arbitrary: it must be a divisor of both the image width and height.

For example, if the image is 800×600 pixels, valid block sizes could be 20, 50, 100, etc., as long as they evenly divide both width and height.

If a non-compatible size is chosen, the process does not work.

**Note**: the block size must be specified both when generating the puzzle and when solving it.

### Usage

```text

bmpuzzle mode [-h] -i INPUT -o OUTPUT -s SECRET [-b BLOCK_SIZE] [-d]

Modes:
    generator
    solver

Flags:
  -h, --help            show this help message and exit

  -i INPUT, --input INPUT
                        Source Image filename
  
  -o OUTPUT, --output OUTPUT
                        Output Image filename
  
  -s SECRET, --secret SECRET
                        Secret value (integer value)
  
  -b BLOCK_SIZE, --block-size BLOCK_SIZE
                        Block size in pixels, format 'widthxheight' (must evenly divide the image size)
  
  -d, --debug           Debug

```

### Generate a Puzzle

```bash

./bmpuzzle generator --input [source image] --output [output image] --secret [secret value] --block-size <block size [widthxheight]>

```

An example:

```bash

./bmpuzzle generator --input images/lena.bmp --output puzzles/100x100.bmp --secret 1234567890 --block-size 100x100

```

https://github.com/user-attachments/assets/b52b562a-79f6-4873-8de5-9a6a66fa6e12

### Solve a Puzzle

```bash

./bmpuzzle solver --input [source image] --output [output image] --secret [secret value] --block-size <block size [widthxheight]>

```

An example:

```bash

./bmpuzzle solver --input puzzles/100x100.bmp --output results/100x100.bmp --secret 1234567890 --block-size 100x100

```

https://github.com/user-attachments/assets/748a0b27-24b4-4008-bbe0-5cd76adb51d8

### Tests

The secret used to generate the puzzles in the folder with the same name is `1234567890`.

### TODO

- DEBUG info
- Data validation

---
