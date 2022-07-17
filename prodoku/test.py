from sudoku_generator import SudokuGenerator

generator1 = SudokuGenerator(rank=3)
generator1.generate_board()
generator1.display_board()

generator2 = SudokuGenerator(rank=2)
generator2.generate_board()
generator2.display_board()
