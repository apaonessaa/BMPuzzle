from src.analyzer import Analyzer

class Block:    
    def __init__(self, analyzer: Analyzer, b_width: int, b_height: int):
        """
        Initializes the Block class, dividing the image into blocks of size (b_width, b_height).
        """
        if analyzer is None and b_width > 0 and b_height > 0:
            raise RuntimeError()

        height, width = analyzer.get_size()

        # Check if the block size is compatible with image size
        if height % b_height > 0 or width % b_width > 0:
            raise RuntimeError()
        
        self.analyzer = analyzer
        self.b_width = b_width
        self.b_height = b_height

        self.nrows = height // self.b_height    # Number of block rows
        self.ncols = width // self.b_width      # Number of block columns
        self.n = self.nrows * self.ncols        # Total number of blocks
        
    def get_properties(self):
        """ Returns the block width and height. """
        return self.b_width, self.b_height
    
    def get_num(self):
        """ Returns the number of rows, columns, and total blocks. """
        return self.nrows, self.ncols, self.n

    def get_location(self, index):
        """ Returns the pixel start coordinates of the block at the given index. """
        _, width = self.analyzer.get_size()
        b_row = (index // self.ncols) * self.b_height * width  # Row start position
        b_col = (index % self.ncols) * self.b_width            # Column start position
        return b_row, b_col
    
    def get_offset(self, index):
        """ Returns the memory offset in the image payload for the given block index. """
        b_row, b_col = self.get_location(index)
        padding = self.analyzer.get_padding()
        Bpp = self.analyzer.get_Bpp()
        return b_row * (Bpp + padding) + b_col * Bpp