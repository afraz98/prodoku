import random

class SudokuGenerator():
    _version = "0.0.0"
    
    def __init__(self, grid_size=9, difficulty='easy', debug=False):
        self.debug = debug
        self.grid_size = grid_size    
        self.difficulty = difficulty

        # Generate default game board
        self.board = [[0 for i in range(self.grid_size)] for i in range(self.grid_size)]
        pass

    def generate_board(self):
        """
        Naive solution: 

        Generate cells at random. Before placing cells, verify that their placement 
        is correct. 
        """

        # Generate values for all random tiles
        
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                valid_cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                value = random.choice(valid_cell_values)
                if self.debug:
                    print("Possible value: %d" % value)
                while not (self._check_row(i, value) and self._check_column(j, value) and self._check_nonet(i, j, value)):
                    value = random.choice(valid_cell_values)
                    if self.debug:
                        print("Possible value: %d" % value)
                
                self.board[i][j] = value
                valid_cell_values.remove(value)
                self.display_board()
            assert(sum(self.board[i]) == 45)
        
        # Remove K cells from the game board.
        pass
    
    def _check_row(self, row_index, value):
        """ Check the provided row to see if the generated value is unused. """
        if self.debug:
            print("Checking row ... %s" % str(self.board[row_index].count(value) == 0))
        return (self.board[row_index].count(value) == 0)

    def _check_column(self, column_index, value):
        """ Check the provided column to see if the generated value is unused. """
        count = 0
        for i in range(0, self.grid_size):
            if self.board[i][column_index] == value:
                count += 1

        if self.debug:
            print("Checking column ... %s" % (str(count==0)))
        return (count == 0)
    
    def _check_nonet(self, row_index, column_index, value):
        """ Check the provided nonet to see if the generated value is unused. """
        nonet_start_row = int(row_index / 3)
        nonet_start_column = int(column_index / 3)

        if self.debug:
            print("start_row: %d start_column: %d" % (nonet_start_row, nonet_start_column))
        for i in range((3 * nonet_start_row), (3 * nonet_start_row) + 3):
            for j in range(3 * nonet_start_column, (3 * nonet_start_column) + 3):
                if self.debug:
                    print("(%d,%d) = %d == %d? %s" % (i, j, self.board[i][j], value, str(self.board[i][j] == value)))
                if self.board[i][j] == value:       
                    return False
        return True


    def _is_solvable(self):
        return True

    def display_board(self):
        for i in range(0, self.grid_size):
            print(*self.board[i])
        print()



