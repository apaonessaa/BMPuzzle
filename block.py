from analyzer import Analyzer

class Block:    
    def __init__(self, analyzer: Analyzer, b_width: int=10, b_height: int=10):
        self.analyzer = analyzer
        self.b_width = b_width
        self.b_height = b_height

        width, height = self.analyzer.get_size()

        self.nrows = width//self.b_height           # num of block rows
        self.ncols = height//self.b_width           # num of block cols
        self.n = self.nrows*self.ncols              # total num of blocks
        
    def get_properties(self):
        return  self.b_width, self.b_height
    
    def get_num(self):
        return  self.nrows, self.ncols, self.n

    # Return block pixel start coordinates
    def get_location(self, index):
        width, _ = self.analyzer.get_size()
        # which block row? self.b_height * width is the full block row amount of pixels
        b_row = (index//self.ncols) * self.b_height * width # pixel
        # which block col?
        b_col = (index%self.ncols) * self.b_width           # pixel
        return b_row, b_col
    
    # Return block offset in payload
    def get_offset(self, index):
        b_row, b_col = self.get_location(index) # pixel
        padding = self.analyzer.get_padding() # data payload row length in bytes
        Bpp = self.analyzer.get_Bpp()
        # 
        #
        return b_row * (Bpp + padding) + b_col * Bpp