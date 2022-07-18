import sys
sys.path.insert(0, "../prodoku")

from sudoku_generator import SudokuGenerator

generator = SudokuGenerator(rank=3, difficulty='easy')
generator.generate_board()
generator.display_board()
print()

generator2 = SudokuGenerator(rank=3, difficulty='medium')
generator2.generate_board()
generator2.display_board()
print()
