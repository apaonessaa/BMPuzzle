# BMPuzzle

BMPuzzle is a command-line tool that transforms BMP images into puzzles and solves them. The project is based on the concept of shuffling image blocks using a predefined sequence and then reconstructing the original image. It relies on the `Analyzer` module from the [apaonessaa/LSBmp](https://github.com/apaonessaa/LSBmp) repository for handling BMP file operations.

<p align="center">
  <img width="640" height="214" alt="puzzle" src="https://github.com/user-attachments/assets/a5cb54e8-b783-4177-8150-606861fd46b4" />
</p>

### Usage

```bash

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
