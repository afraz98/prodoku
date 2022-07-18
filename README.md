# prodoku

`prodoku` is an all-in-one Sudoku implementation native to Python-3. It offers puzzle-generation, puzzle-solving, and solution validation.

## Background

Sudoku is a puzzle game that provides the player with a 9x9 grid containing numbers between 1 and 9. The player must fill all spaces with numbers under the following conditions:

1) Each row must contain all numbers between 1 - 9 with no repetitions. 

2) Each column must contain all numbers between 1 - 9 with no repetitons.

3) Each nonet (3 x 3 grid) must contain all numbers between 1 - 9 with no repetitions.

## Features

1) SudokuGenerator

2) SudokuSolver

3) SudokuValidator

## Usage

```
generator = SudokuGenerator(rank=3, difficulty='easy')
generator.generate_board()
generator.display_board()
```

Output:

```
6 1 0 8 9 5 4 3 2
8 5 9 2 0 3 7 1 0
2 3 0 6 0 1 9 0 8
1 0 8 5 2 9 6 4 3
3 4 6 1 8 7 2 9 5
5 9 2 3 6 4 8 7 1
9 2 3 4 1 0 5 8 7
7 8 5 0 3 2 1 6 4
4 0 1 7 5 8 3 2 9
```

```
test_board = [
    [0, 0, 8, 1, 0, 7, 2, 0, 4],
    [9, 0, 0, 0, 5, 8, 6, 1, 0],
    [1, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 1, 8, 2, 9],
    [6, 4, 0, 2, 8, 9, 7, 0, 3],
    [2, 8, 0, 5, 7, 0, 4, 6, 1],
    [7, 1, 0, 0, 0, 6, 3, 8, 2],
    [0, 0, 6, 8, 3, 0, 1, 7, 5],
    [8, 3, 0, 7, 1, 5, 9, 4, 6],
]

solver = SudokuSolver(test_board)
solver.solve()
```

Output:

```
3 5 8 1 6 7 2 9 4
9 2 4 3 5 8 6 1 7
1 6 7 9 2 4 5 3 8
5 7 3 6 4 1 8 2 9
6 4 1 2 8 9 7 5 3
2 8 9 5 7 3 4 6 1
7 1 5 4 9 6 3 8 2
4 9 6 8 3 2 1 7 5
8 3 2 7 1 5 9 4 6
```

## Installation

``` sudo python3 setup.py install ```


