import sys
sys.path.insert(0, "../prodoku")

from sudoku_solver import SudokuSolver
from sudoku_generator import SudokuGenerator

# Generate 'easy' board
generator = SudokuGenerator(rank=3, difficulty='easy')
generator.generate_board()
generator.display_board()
print()

# Attempt to solve board
solver = SudokuSolver(generator.get_board())
solver.solve()
print()

# Generate 'hard' board
generator = SudokuGenerator(rank=3, difficulty='hard')
generator.generate_board()
generator.display_board()
print()

# Attempt to solve board
solver = SudokuSolver(generator.get_board())
solver.solve()
print()