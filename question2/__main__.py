import sys

from triangle import triangle
from frame import frame
from chessboard import chessboard

if __name__ == '__main__':
   matrix_size = int(sys.argv[1])
   triangle(matrix_size)
   frame(matrix_size)
   chessboard(matrix_size)