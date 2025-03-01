# BMPuzzle

BMPuzzle is a command-line tool that transforms BMP images into puzzles and solves them. The project is based on the concept of shuffling image blocks using a predefined sequence and then reconstructing the original image. It relies on the `Analyzer` module from the [apaonessaa/LSBmp](https://github.com/apaonessaa/LSBmp) repository for handling BMP file operations.

## Features
- **Puzzle Generator:** Splits a BMP image into shuffled blocks based on a seed.
- **Puzzle Solver:** Reconstructs the original image from the shuffled blocks.
- **Custom Key Support:** Uses a user-defined key to generate a consistent puzzle sequence.
- **BMP Format Handling:** Ensures compatibility with BMP image format.

## Dependencies
- Python 3
- Optional: ImageMagick (for image format conversion and previewing results)

## Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/BMPuzzle.git
cd BMPuzzle
```

## Usage

### Generate a Puzzle
```bash
./generator <image.bmp> -k <key>
```
Example:
```bash
./generator images/tiger.bmp -k secret
```
This will generate a shuffled puzzle image inside the `puzzles/` directory.

### Solve a Puzzle
```bash
./solver <puzzle.bmp> -k <key>
```
Example:
```bash
./solver puzzles/puzzle_0.bmp -k secret
```
This reconstructs the original image and saves it inside the `results/` directory.

## Example Execution
_A demo video will be included here to showcase how the tool works._

## Upcoming Features
- **Custom Block Size:** Allow users to specify block dimensions. (Must be multiples of the input image dimensions.)
- **Input Validation:** Handle errors related to incompatible block sizes and image dimensions.
- **Enhanced Error Handling:** Improve feedback for invalid inputs and missing dependencies.

## License
This project is open-source and available under the MIT License.

---

For any issues or feature requests, feel free to open an issue on the repository.
