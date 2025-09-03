# **BMPuzzle**

**BMPuzzle** is a command-line tool that transforms BMP images into puzzles and allows you to solve them. 

The core idea is to split the image into blocks, shuffle them according to a sequence generated from a **secret**, and then use the same secret to reconstruct the original image.

![bmpuzzle](./bmpuzzle.png)

## **How it works**

1. The image is divided into square blocks.
2. The blocks are shuffled following an order derived from a secret (a key/seed).
3. To rebuild the image, you need to provide the same secret: this ensures that the blocks are placed back in their original position.

## **Block size selection**

The block size cannot be arbitrary: it must be a divisor of both the image width and height.

For example, if the image is 800×600 pixels, valid block sizes could be 20, 50, 100, etc., as long as they evenly divide both width and height.

If a non-compatible size is chosen, the process does not work correctly.

**Note**: the block size must be specified both when generating the puzzle and when solving it.

Below is an example of the tool's application.

## **Generate a Puzzle**

In this example, we use the image `lena.bmp` with dimensions **1200x800**. A valid block size is **300x200**.

```bash

./bmpuzzle generator --input lena.bmp --output puzzles/300x200.bmp --secret 1234567890 --block-size 300x200

```

![bmpuzzle generation](./gen.png)

## **Solve a Puzzle**

First, solve the puzzle using the correct secret.

```bash

./bmpuzzle solver --input puzzles/300x200.bmp --output results/300x200.bmp --secret 1234567890 --block-size 300x200

```

![bmpuzzle solved](./solv.png)

Whereas, if the key used for solving does not match the one used for generation, the puzzle will be shuffled.

![bmpuzzle wrong key](./wrong_key.png)

See more information on the **Github page**.

---


