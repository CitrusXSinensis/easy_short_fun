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

grid1x1_1 = [[False]]

grid1x3 = [[True,False,True]]

grid3x3 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

grid4x5 = [[False,True,False,False,False],
           [False,False,False,False,True],
           [False,False,True,False,False],
           [False,False,False,False,False]]

board1x1 = [[' ']]

board1x1_1 = [['*']]

board1x1_2 = [['0']]

board1x3 = [[' ','2',' ']]

board3x3 = [[' ', '1', '0'],
            [' ', '2', '1'],
            [' ', ' ', '*']]

board3x3_1 = [[' ', '1', '0'],
              ['1', '2', '1'],
              ['0', '1', ' ']]

board3x3_2 = [[' ', '1', '0'],
              ['1', '2', '1'],
              ['0', ' ', ' ']]

board3x3_3 = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

board3x3_4 = [[' ', '1', '0'],
              ['1', ' ', '1'],
              ['0', '1', ' ']]

board4x5 = [['1', '*', '1', '1', '1'],
            ['1', '2', '2', '2', ' '],
            [' ', '1', ' ', '2', '1'],
            ['0', '1', '1', '1', '0']]

board4x5_1 = [['1', ' ', '1', '1', '1'],
              ['1', '2', '2', '2', ' '],
              [' ', '1', ' ', '2', '1'],
              [' ', '1', '1', '1', '0']]

board4x5_2 = [['1', ' ', '1', '1', '1'],
              ['1', '2', '2', '2', ' '],
              ['0', '1', ' ', '2', '1'],
              ['0', '1', '1', '1', '0']]

board4x5_3 = [[' ', '*', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ']]

board4x5_4 = [['1', ' ', '1', '1', '1'],
              ['1', '2', '2', '2', ' '],
              ['0', '1', ' ', '2', '1'],
              ['0', '1', '1', '1', ' ']]
# game_lost(board) returns true if board contains one or more revealed mines,
#   false otherwise
# game_lost: GameBoard -> Bool

def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0

# convert_board(board_row) returns True if element is ' ', else returns False
# convert_board: Str -> Bool
# Requires:  string should be either a hidden(' ')
#             or safe (a digit between '0' and '8')
# Examples:
# convert_board('8') => False
# convert_board('1') => False
# convert_board(' ') => True

def convert_board(element):  
    if element[0] == ' ':
        return True
    else: return False
    
# game_won(grid,board)
# game_won: MineGrid MineBoard -> Bool
# requires: grid and board have the same dimensions and are consistent
# Examples:
# game_won(grid3x3,board3x3) => False
# game_won(grid3x3,board3x3_1) => True
# game_won(grid3x3,board3x3_2) => False
    
def game_won(grid,board):
    if game_lost(board): return False
    elif len(grid) == 1 and list(map(convert_board,board[0])) == grid[0]:
        return True
    elif list(map(convert_board,board[0])) != grid[0]:
        return False
    else:
        return game_won(grid[1:],board[1:])
    
# Tests:
check.expect("test1",game_won(grid3x3,board3x3),False)
check.expect("test2",game_won(grid3x3,board3x3_1),True)
check.expect("test3",game_won(grid3x3,board3x3_2),False)
check.expect("test4",game_won(grid3x3,board3x3_3),False)
check.expect("test5",game_won(grid4x5,board4x5),False)
check.expect("test6",game_won(grid4x5,board4x5_1),False)
check.expect("test7",game_won(grid4x5,board4x5_2),True)
check.expect("test8",game_won(grid4x5,board4x5_3),False)
check.expect("test9",game_won(grid4x5,board4x5_4),False)
check.expect("test10",game_won(grid3x3,board3x3_4),False)
check.expect("test11",game_won(grid1x1,board1x1),True)
check.expect("test12",game_won(grid1x1,board1x1_1),False)
check.expect("test13",game_won(grid1x1_1,board1x1),False)
check.expect("test13",game_won(grid1x1_1,board1x1_2),True)
check.expect("test14",game_won(grid1x3,board1x3),True)
