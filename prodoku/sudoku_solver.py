class SudokuSolver():
    """
    This class solves Sudoku boards of a given rank and difficulty.
    A Sudoku board is represented by an n^2 x n^2 grid where n is the rank of the board. 
    This means a typical 9x9 Sudoku grid would have rank n = 3.

    The easiest method to generate a Sudoku board would be to first a 'solved' 9x9 Sudoku grid
    and remove K elements from this grid. 

    Attributes:
        rank (int): The rank of the Sudoku board to be generated. For an n^2 x n^2 board, its rank would be n.
        debug (bool): Debug flag
        board (list): List representation of the n^2 x n^2 game board to be solved. 
        analysis_board (list): n^2 x n^2 list storing all possible values that may
                                be entered into a given cell. 
    """
    _version = "0.0.1"
    
    def __init__(self, board, rank=3, debug=True):
        self.board = board
        self.rank = rank
        self.grid_size = self.rank * self.rank
        self.debug = debug

        # Create a representation of the game board with a list of possible values mapped to each game board cell. 
        self.analysis_board = [ [[1,2,3,4,5,6,7,8,9] for i in range(self.grid_size)] for i in range(self.grid_size)]
        pass

    def display_board(self):
        """ Display the game board. """
        for i in range(0, self.grid_size):
            print(*self.board[i])    
        print() 
        pass

    def solve(self):
        """
        Attempt to solve the provided Sudoku puzzle. Looks at each cell on the game board and determine which 
        values may be placed in them. If any cells have trivial entries (where only one value can be entered), enter them.

        Returns:
            (int): Number of iterations through the naive algorithm 
                    required to find the given solution. 
        """
        if self.debug:
            self.display_board()
        
        iterations = 1
        while not self._check_board():

            # Start with naive approach -- look at each cell on the game board and determine which 
            # values may be placed in them. If any cells have trivial entries, enter them. 
            for i in range(0, self.grid_size):
                for j in range(0, self.grid_size):
                    self.analysis_board[i][j] = self._analyze_cell(i, j)

            # If any trivial cases are found, fill in the cells with the corresponding values.
            for i in range(0, self.grid_size):
                for j in range(0, self.grid_size):
                    if len(self.analysis_board[i][j]) == 1:
                        if self.debug:
                            print("(%d, %d) = %d" % (i, j, self.analysis_board[i][j][0]))
                        self.board[i][j] = self.analysis_board[i][j][0]
                        self.analysis_board[i][j] = []

            if self.debug:
                print("Iteration %d" % iterations)
                self.display_board()
                input()

            iterations += 1
        
        if self.debug:
            print("Solution")
            self.display_board()
        
        return iterations

    def _analyze_cell(self, row_index, column_index):
        """
        Analyze a given cell to determine what values may 
        be validly placed within the cell. 

        Args:
            row_index (int): Row of the cell to be analyzed. 
            column_index (int): Column of the cell to be analyzed. 
        Returns:
            (list): List of possible cell values. 
        """
        if self.board[row_index][column_index] != 0:
            return []

        possible_cell_values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        for value in range(1,10):
            if self._check_row_for_value(row_index, value) or self._check_column_for_value(column_index, value) or self._check_nonet_for_value(row_index, column_index, value):
                possible_cell_values.remove(value)
        return possible_cell_values
    
    def _check_row_for_value(self, row_index, value):
        """
        Check to see if a value is present within a given row.

        Args:
            row_index (int): Row that will be checked for the provided value.
            value (int): Value to search the given row for.
        Returns:
            (bool): Flag indicated that value IS within the row.
        """
        return value in self.board[row_index]

    def _check_column_for_value(self, column_index, value):
        """
        Check to see if a value is present with a given column.

        Args:
            column_index (int): Column that will be checked for the provided value.
            value (int): Value to search the given column for.
        Returns:
            (bool): Flag indicated that value IS within the column.
        """
        return value in [ self.board[i][column_index] for i in range(0, self.grid_size) ]

    def _check_nonet_for_value(self, row_index, column_index, value):
        """
        Check to see if a value is present with a given nonet, (sub-3x3 grid).

        Args:
            row_index (int): Row that will be checked for the provided value.
            column_index (int): Column that will be checked for the provided value.
            value (int): Value to search the given column for.
        Returns:
            (bool): Flag indicated that value IS within the nonet.
        """
        nonet_start_row = row_index // 3
        nonet_start_column = column_index // 3

        for i in range((3 * nonet_start_row), (3 * nonet_start_row) + 3):
            for j in range(3 * nonet_start_column, (3 * nonet_start_column) + 3):
                if self.board[i][j] == value:       
                    return True
        return False

    def _check_row_accuracy(self, row_index):
        return sum(self.board[row_index]) == 45

    def _check_column_accuracy(self, column_index):
        sum = 0
        for i in range(0, self.grid_size):
            sum += self.board[i][column_index]
        return sum == 45

    def _check_nonet_accuracy(self, row_index, column_index):
        sum = 0
        for i in range(row_index, row_index+3):
            for j in range(column_index, column_index+3):
                sum += self.board[i][j]
        return sum == 45

    def _check_board(self):
        """ 
            Check the game board to see if a solution has been found. 

            A solution can be said to be 'found' if for all rows, columns, and nonets x the following holds:
                1. The sum of all elements in x is 45. 
                2. x contains ONLY unique numbers between 1 and 9 (follows from (1)). 
        """
        result = True

        # Iterate through rows and columns, checking sum of elements
        for i in range(0, self.grid_size):
            result &= self._check_column_accuracy(i)
            result &= self._check_row_accuracy(i)

        if not result:
            return False

        # Iterate through nonets, checking sum of elements
        for i in range(0, self.grid_size, 3):
            for j in range(0, self.grid_size, 3):
                result &= self._check_nonet_accuracy(i, j) 
        
        return result

class KillerSudokuSolver(SudokuSolver):
    _version = "0.0.0"
    def __init__(self, board, rank=3, debug=True):
        pass

