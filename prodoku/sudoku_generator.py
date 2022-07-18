import random

class SudokuGenerator():
    """
    This class generates Sudoku boards of a given rank and difficulty.
    A Sudoku board is represented by an n^2 x n^2 grid where n is the rank of the board. 
    This means a typical 9x9 Sudoku grid would have rank n = 3.

    The easiest method to generate a Sudoku board would be to first a 'solved' 9x9 Sudoku grid
    and remove K elements from this grid. 

    Attributes:
        rank (int): The rank of the Sudoku board to be generated. For an n^2 x n^2 board, its rank would be n.
        debug (bool): Debug flag
        difficulty (str): String representing the 'difficulty' of the puzzle to be generated. 
                            this determines K, the number of elements removed from the grid. 
    """
    _version = "0.0.1"


    # Puzzle difficulty is determined by the number of cells removed from the puzzle. 
    # Currently supports three different difficulty levels. 
    _DIFFICULTY_MAPPING = { 'easy': 10, 'hard': 30 }

    
    def __init__(self, rank=3, difficulty='easy', debug=True):
        self.debug = debug
        self.rank = rank   
        self.side = self.rank * self.rank

        self.difficulty = difficulty
        self.K = self._DIFFICULTY_MAPPING[self.difficulty]
        pass

    # Pattern for a baseline valid solution
    def pattern(self, r,c): 
        return (self.rank * (r % self.rank) + r // self.rank + c) % self.side

    def shuffle(self, s): 
        return random.sample(s, len(s)) 

    def generate_board(self):
        """ Start by generating a random filled-in game-board following Sudoku rules.
        Adapted from the following: https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python """
        # Randomize rows, columns and numbers (of valid base pattern)
        rows  = [ g * self.rank + r for g in self.shuffle(range(self.rank) ) for r in self.shuffle(range(self.rank) ) ] 
        cols  = [ g * self.rank + c for g in self.shuffle(range(self.rank) ) for c in self.shuffle(range(self.rank) ) ]
        nums  = self.shuffle(range(1, self.rank * self.rank +1))

        # Produce board using randomized baseline pattern
        self.board = [ [nums[ self.pattern(r, c) ] for c in cols ] for r in rows ]
        
        """ After a valid, filled-in game-board has been generated, remove K cells from the game-board to create the puzzle. """
        K = 0
        while(K < self.K):
            removed = self._remove_random_cell()
            if removed:
                K += 1
        pass
    
    def _remove_random_cell(self):
        """ Remove random cell from the game board. """
        i = random.randint(0, self.side - 1)
        j = random.randint(0, self.side - 1)
        if self.board[i][j] == 0:
            return False
        self.board[i][j] = 0
        return True

    def _is_solvable(self):
        """ Check if the given Sudoku puzzle generated is solvable. """
        raise NotImplementedError("Not yet implemented")

    def get_board(self):
        return self.board

    def display_board(self):
        """ Display Sudoku board. """
        for i in range(0, len(self.board)):
            print(*self.board[i])


class KillerSudokuGenerator(SudokuGenerator):
    _version = "0.0.0"
    def __init__(self, rank=3, difficulty='easy', debug=True):
        pass

