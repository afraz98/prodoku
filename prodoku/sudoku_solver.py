class SudokuSolver():
    _version = "0.0.0"
    
    def __init__(self, board, rank=3, debug=True):
        self.board = board
        self.rank = rank
        self.grid_size = self.rank * self.rank
        self.debug = debug

        # Create a representation of the game board with a list of possible values 
        # mapped to each game board cell. 
        self.analysis_board = [ [[1,2,3,4,5,6,7,8,9] for i in range(self.grid_size)] for i in range(self.grid_size)]
        pass

    def display_board(self):
        for i in range(0, self.grid_size):
            print(*self.board[i])    
        print() 
        pass

    def solve(self):
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
        
        pass

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
        return self.board[row_index].count(value) != 0

    def _check_column_for_value(self, column_index, value):
        """
        Check to see if a value is present with a given column.

        Args:
            column_index (int): Column that will be checked for the provided value.
            value (int): Value to search the given column for.
        Returns:
            (bool): Flag indicated that value IS within the column.
        """
        count = 0
        for i in range(0, self.grid_size):
            if self.board[i][column_index] == value:
                count += 1
        return count != 0

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
        nonet_start_row = int(row_index/3)
        nonet_start_column = int(column_index/3)

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

