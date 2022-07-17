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

    def solve(self):
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

        possible_cell_values = [1,2,3,4,5,6,7,8,9]
        for value in possible_cell_values:
            if self._check_row_for_value(row_index, value) or self._check_column_for_value(column_index, value):
                possible_cell_values.remove(value)
        return possible_cell_values
    
    def _check_row_for_value(self, row_index, value):
        """
        Check to see if a value is present within a given row.

        Args:
            row_index (int): Row that will be checked for the provided value.
            value (int): Value to search the given row for.
        """
        return self.board[row_index].count(value) == 0

    def _check_column_for_value(self, column_index, value):
        """
        Check to see if a value is present with a given column.

        Args:
            column_index (int): Column that will be checked for the provided value.
            value (int): Value to search the given column for.
        """
        count = 0
        for i in range(0, self.grid_size):
            if self.board[i][column_index] == value:
                count += 1
        return (count == 0)

