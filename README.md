# BMPuzzle

BMPuzzle is a command-line tool that transforms BMP images into puzzles and solves them. The project is based on the concept of shuffling image blocks using a predefined sequence and then reconstructing the original image. It relies on the `Analyzer` module from the [apaonessaa/LSBmp](https://github.com/apaonessaa/LSBmp) repository for handling BMP file operations.

### Usage

```bash

BMPuzzle mode [-h] -i INPUT -o OUTPUT -s SECRET [-b BLOCK_SIZE] [-d]

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
                        Block size in pixels, format 'heightxwidth' (must evenly divide the image size)
  
  -d, --debug           Debug

```

### Generate a Puzzle

```bash

./bmpuzzle generator --input [source image] --output [output image] --secret [secret value] --block-size <block size [heightxwidth]>

```

An example:

```bash

./bmpuzzle generator --input images/lena.bmp --output puzzles/100x100.bmp --secret 1234567890 --block-size 100x100

```

[photo]

### Solve a Puzzle

```bash

./bmpuzzle solver --input [source image] --output [output image] --secret [secret value] --block-size <block size [heightxwidth]>

```

An example:

```bash

./bmpuzzle solver --input puzzles/100x100.bmp --output results/100x100.bmp --secret 1234567890 --block-size 100x100

```

[photo]

### Example Execution

[video]

### TODO

- DEBUG info
- Data validation

---