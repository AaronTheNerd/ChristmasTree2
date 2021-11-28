class Color:
    def __init__(self, r, g, b):
        self.r = r & 0xFF
        self.g = g & 0xFF
        self.b = b & 0xFF

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)