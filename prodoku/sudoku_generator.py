import random

class SudokuGenerator():
    """
    Difficulty mappings:
        1) Easy (K = 20)
        2) Medium (K = 30)
        3) Hard (K = 40)
    """

    _difficulty_mapping = {
        'easy': 10,
        'medium': 30,
        'hard': 50
    }

    _version = "0.0.1"
    
    def __init__(self, base=3, difficulty='easy', debug=True):
        self.debug = debug
        self.base = base   
        self.side = self.base * self.base

        self.difficulty = difficulty
        self.K = self._difficulty_mapping[self.difficulty]
        pass

    # pattern for a baseline valid solution
    def pattern(self, r,c): 
        return (self.base * (r % self.base)+ r // self.base + c) % self.side

    def shuffle(self, s): 
        return random.sample(s, len(s)) 

    def generate_board(self):
        """
        Start by generating a random filled-in game-board following Sudoku rules.
        Adapted from the following: https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
        """
        # Randomize rows, columns and numbers (of valid base pattern)
        rows  = [ g * self.base + r for g in self.shuffle(range(self.base) ) for r in self.shuffle(range(self.base) ) ] 
        cols  = [ g * self.base + c for g in self.shuffle(range(self.base) ) for c in self.shuffle(range(self.base) ) ]
        nums  = self.shuffle(range(1, self.base * self.base +1))

        # Produce board using randomized baseline pattern
        self.board = [ [nums[ self.pattern(r, c) ] for c in cols ] for r in rows ]
        
        """ After a valid, filled-in game-board has been generated, remove K cells from the game-board to create 
        the puzzle. You should keep at least 17 valid cells for a game to be solvable. """
        K = 0
        while(K < self.K):
            removed = self._remove_cell()
            if removed:
                K += 1
        pass
    
    def _remove_cell(self):
        i = random.randint(0, self.side - 1)
        j = random.randint(0, self.side - 1)
        if self.board[i][j] == 0:
            return False
        self.board[i][j] = 0
        return True

    def _is_solvable(self):
        """ Check if the given Sudoku puzzle generated is solvable. """
        raise NotImplementedError("Not yet implemented")

    def display_board(self):
        """ Display Sudoku board """
        for i in range(0, len(self.board)):
            print(*self.board[i])
        print()



