from sudoku_generator import SudokuGenerator
from sudoku_solver import SudokuSolver

generator = SudokuGenerator(rank=3)
generator.generate_board()
generator.display_board()

test_board = [
    [0, 4, 3, 9, 5, 2, 8, 6, 1],
    [2, 9, 5, 8, 0, 6, 4, 7, 3],
    [6, 8, 1, 4, 0, 7, 9, 2, 5],
    [3, 6, 4, 0, 9, 5, 2, 1, 8],
    [5, 7, 9, 2, 8, 0, 6, 3, 0],
    [1, 0, 8, 6, 4, 3, 7, 5, 9],
    [8, 5, 0, 1, 6, 4, 3, 9, 7],
    [9, 3, 7, 5, 0, 8, 1, 4, 6],
    [4, 1, 6, 3, 0, 9, 5, 8, 2],
]

solver = SudokuSolver(test_board)
solver.solve()