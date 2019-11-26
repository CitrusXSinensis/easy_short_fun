import check

# A MineGrid is a (listof (listof Bool))
# Requires:  All lists are non-empty
#            Each (listof Bool) has the same length 

# note: True means mine, False means safe

# A MineBoard is a (listof (listof Str))
# Requires: Each string is either a mine ('*') hidden(' ')
#             or safe (a digit between '0' and '8')
#           All lists are non-empty
#           Each (listof Str) has the same length

# constants

grid1x1 = [[True]]

grid1x3 = [[True,False,True]]

grid2x2 = [[True,False],
           [False,False]]

grid3x3 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

grid5x6 = [[True ,True,True,False,False,False],
           [True,False,True,False,False,True],
           [True,True,True,True,False,False],
           [False,False,False,False,False,False],
           [True,False,True,False,False,True]]

board3x3 = [[' ', '1', '0'],
            [' ', '2', '1'],
            [' ', ' ', '*']]

# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated

def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))

# count_mines_area(grid,row,col) returns a list of boolean which represents
#   the booleans nearby the element in grid located at row and col (column) 
#   given
# count_mines_area: MineGrid Nat Nat -> (listof Bool)
# requires: 0 <= row < height of grid
#           0 <= col < width  of grid
# Examples:
# count_mines_area(grid3x3,1,2) => [False, False, False, False, True]
# count_mines_area(grid3x3,0,0) => [False, False, False]

def count_mines_area(grid,row,col):
    row_num = len(grid) - 1
    col_num = len(grid[0]) - 1
    if row == 0:
        if col == 0:
            return [grid[0][1]] + grid[1][0:2]
        elif col == col_num:
            return [grid[0][col - 1]] + grid[1][col - 1:col + 1]
        else:
            return [grid[0][col - 1]] + [grid[0][col + 1]] + grid[1]\
                   [col - 1:col + 2]
    elif row == row_num:
        if col == 0:
            return [grid[row][1]] + grid[row - 1][0:2]
        elif col == col_num:
            return [grid[row][col - 1]] + grid[row - 1][col - 1:col + 1]           
        else:
            return [grid[row][col - 1]] + [grid[row][col + 1]] +\
                   grid[row - 1][col - 1:col + 2]
    else:
        if col == 0:
            return grid[row - 1][0:2] + grid[row + 1][0:2] + [grid[row][1]]          
        elif col == col_num:
            return [grid[row][col - 1]] + grid[row - 1][col - 1:col + 1] +\
                   grid[row + 1][col - 1:col + 1]
        else:
            return [grid[row][col - 1]] + grid[row - 1][col - 1:col + 2] +\
                   grid[row + 1][col - 1:col + 2] + [grid[row][col + 1]]


# count_mines(grid,row,col) returns the number of mines around an element in 
#   grid which located at row and col (column) given 
# count_mines: MineGrid Nat Nat -> Nat
# requires: 0 <= row < height of grid
#           0 <= col < width  of grid
# Examples: 
# count_mines(grid3x3,0,0) => 0
# count_mines(grid3x3,1,0) => 1
# count_mines(grid3x3,1,1) => 2

def count_mines(grid,row,col):
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    elif len(grid) == 1:
        if col == 0: return int(grid[0][1])
        elif col == len(grid[0]) - 1: return int(grid[0][-2])
        else: return int(grid[0][col - 1]) + int(grid[0][col + 1])
    else:
        return len(list(filter(lambda x: x == True,count_mines_area\
                               (grid,row,col))))

# Tests:
check.expect("test1",count_mines(grid3x3,0,0),0)
check.expect("test2",count_mines(grid3x3,1,0),1)
check.expect("test3",count_mines(grid3x3,2,0),0)
check.expect("test4",count_mines(grid3x3,0,1),1)
check.expect("test5",count_mines(grid3x3,1,1),2)
check.expect("test6",count_mines(grid3x3,2,1),1)
check.expect("test7",count_mines(grid3x3,0,2),0)
check.expect("test8",count_mines(grid3x3,1,2),1)
check.expect("test9",count_mines(grid3x3,2,2),0)
check.expect("test10",count_mines(grid5x6,4,5),0)
check.expect("test11",count_mines(grid5x6,1,1),8)
check.expect("test12",count_mines(grid5x6,0,0),2)
check.expect("test13",count_mines(grid5x6,3,0),3)
check.expect("test14",count_mines(grid5x6,3,3),3)
check.expect("test15",count_mines(grid2x2,1,0),1)
check.expect("test16",count_mines(grid2x2,0,0),0)
check.expect("test17",count_mines(grid1x1,0,0),0)
check.expect("test18",count_mines(grid1x3,0,1),2)
check.expect("test18",count_mines(grid1x3,0,2),0)
