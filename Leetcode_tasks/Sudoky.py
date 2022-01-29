def solveSudoku(board):
    """
    Modify table 9x9 by numbers from 1 to 9 so that none of rows, none of columns and none of blocks 3x3 contain repeating digits. Empty cells have value '.'
    param board: list containing 9 lists each of them contains 9 elements
    return: table without empty cells. Only elements from 1 to 9
    """
    short_list = [str(digit) for digit in range(1, 10)]  # create list from numbers from 1 to 9. These variables are string
    # Run to each element (col) of each internal list (row) consequentially
    for row in range(9):
        for col in range(9):
            # If the current cell is empty ('.') it needs to be completed by digit
            if board[row][col] == '.':
                # divide the board into tables 3x3. To do this it necessary:
                # define start of the block (index is multiple of 3). The current index is divided by 3 and integer part of the result is multiplied by 3
                # define ending of the block (index is 2 more than start and it is included). Right border is 3 more than left
                # create current block 3x3 where there is a current cell
                mini_table = sum([[board[row][col] for col in range(col//3*3, col//3*3+3)] for row in range(row//3*3, row//3*3+3)], [])
                # create list from elements of the column where there is a current cell
                column = list(list(zip(*board))[col])
                # list from elements of the row where there is a current cell is the current index of the board
                # Run to each elements of variable 'short_list'
                for number in short_list:
                    # each number mustn't be in row, in column and in block 3x3 together where the current cell is located
                    if number not in board[row] and number not in column and number not in mini_table:
                        board[row][col] = number  # if this condition is true the current cell is filled by current number
                        # complete the board by recursion
                        if solveSudoku(board):
                            return board  # recursion is succeeded. Table is completed
                        else:
                            board[row][col] = '.'  # if either of row, column or block will have repeating elements let's back to the current element and take it empty
                return False  # none of digits can be on this cell in current moment. Move to the next cell
    return board  # return completed table
