import check

# ## a Bingocard is a (dictof Str (listof (anyof Nat 'XX'))) and 		
# ## represents a standard bingo card in 75 ball bingo
# ## requires: 
# ##	- it has exactly 5 key value pairs
# ##	- the keys are the capital letters 'B' 'I' 'N' 'G' 'O'
# ## 	- each list is length 5 and is made up of the string 'XX' or 
# ##	  numbers 1 through 75 according to the breakdown below
# ##	- key 'B' only has numbers between 1 and 15 inclusive 
# ##	- key 'I' only has numbers between 16 and 30 inclusive
# ##	- key 'N' only has numbers between 31 and 45 inclusive
# ##	- key 'G' only has numbers between 46 and 60 inclusive
# ##	- key 'O' only has numbers between 61 and 75 inclusive
# ##	- the associated list at key 'N' will always have its element at 
# ##	  index 2 equal to 'XX' (representing the free space)
# ##	- the numbers in each list must be unique

# constants for testing
bcard = {'O': [73, 61, 64, 72, 70], 'I': [29, 27, 28, 21, 17], \
         'N': [33, 40, 'XX', 42, 43], 'B': [13, 8, 5, 15, 1], \
         'G': [49, 55, 60, 56, 54]}

bgo_crd = {'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26],\
           'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10],\
           'G': [56, 53, 'XX', 47, 52]}

my_card = {'O': [65, 62, 'XX', 64, 74], 'I': [22, 25, 'XX', 20, 26],\
           'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'],\
           'G': [55, 60, 'XX', 53, 56]}

my_card_1 = {'O': [65, 62, 'XX', 64, 74], 'I': [22, 25, 'XX', 20, 26],\
           'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 14, 'XX', 'XX', 'XX'],\
           'G': [55, 60, 'XX', 53, 56]}

row_win = "Winner: Row {0}."
column_win = "Winner: Column {0}."
no_win = "Not a winner."

# display_bingo_card(crd) prints a nicely formatted version of crd
# Effects: 6 lines are printed
# display_bingo_card: Bingocard -> None

def display_bingo_card(crd):
    header = "  B  I  N  G  O  "
    print(header)
    for i in range(5):
        line = " {0:2} {1:2} {2:2} {3:2} {4:2}  ".format(crd['B'][i],
                                                         crd['I'][i],
                                                         crd['N'][i],
                                                         crd['G'][i],
                                                         crd['O'][i])
        print(line)

# mutate_crd(letter,crd,num) returns none, but mutating crd by changing the
#   number in crd[letter] which equals num to 'XX'
# Effects: crd is mutated
# mutate_crd: (anyof 'B' 'I' 'N' 'G' 'O') Bingocard Nat -> None
# requires: num is between 1 and 75 (inclusive)

def mutate_crd(letter,crd,num):
    for i in list(range(5)):
        if crd[letter][i] == num: crd[letter][i] = 'XX'

# play_bingo(crd,lon) mutates crd based on natural numbers in lon, and when a
#   completed row or column is filled with 'XX', stops mutation and return a
#   string that states the winning row/column, otherwise, return no winner
# Effects: crd is mutated
# play_bingo: Bingocard (listof Nat) -> Str
# requires: 0 < lon[i] < 76 for 0 <= i < len(lon)
# Examples:
# play_bingo(bgo_crd,[]) => 'Not a winner'
# play_bingo(bcard,[29,27,45,15,61,17,60,21,13,28,70,33]) => 'Winner: Column I.'
#   and mutate bcard to {'O':[73,'XX',64,72,70],'I': ['XX','XX','XX','XX','XX'],
#   'N':[33,40,'XX',42,43],'B':['XX',8,5,'XX',1],'G':[49,55,'XX',56,54]}
# play_bingo(bgo_crd,[6]) => 'Winner: Row 3.' and mutate bgo_car to
#   {'O':[61,72,'XX',67,74],'I':[25,23,'XX',20,26],'N':[43,38,'XX',36,40],
#   'B':['XX','XX','XX','XX',10],'G':[56,53,'XX' 47,52]}
        
def play_bingo(crd,lon):
    if lon == []: return no_win
    for num in lon:
        if 1 <= num <= 15 and num in crd['B']: mutate_crd('B',crd,num)
        if 16 <= num <= 30 and num in crd['I']: mutate_crd('I',crd,num)
        if 31 <= num <= 45 and num in crd['N']: mutate_crd('N',crd,num)
        if 46 <= num <= 60 and num in crd['G']: mutate_crd('G',crd,num)
        if 61 <= num <= 75 and num in crd['O']: mutate_crd('O',crd,num)
        for i in ['B','I','N','G','O']:
            if crd[i] == ['XX','XX','XX','XX','XX']: 
                return column_win.format(i)
        for i in list(range(5)):
            if [crd['B'][i],crd['I'][i],crd['N'][i],crd['G'][i],crd['O'][i]]\
               == ['XX','XX','XX','XX','XX']: return row_win.format(i + 1)
    return no_win

# Tests:
check.expect('t0',play_bingo(bcard,[75]),no_win)
check.expect('t0_mut',bcard,{'O':[73,61,64,72,70],'I':[29,27,28,21,17],\
                                'N':[33,40,'XX',42,43],'B':[13,8,5,15,1],\
                                'G':[49,55,60,56,54]})
check.expect('t1',play_bingo(bcard,[]),no_win)
check.expect('t1_mut',bcard,{'O':[73,61,64,72,70],'I':[29,27,28,21,17],\
                                'N':[33,40,'XX',42,43],'B':[13,8,5,15,1],\
                                'G':[49,55,60,56,54]})
check.expect('t2',play_bingo(bcard,[29,27,45,15,61,17,60,21,13,28,70,33]),\
            'Winner: Column I.')
check.expect('t2_mut',bcard,{'O':[73,'XX',64,72,70],'I':['XX','XX','XX',\
                                                            'XX','XX'],\
                                'N':[33,40,'XX',42,43],'B':['XX',8,5,'XX',1],\
                                'G':[49,55,'XX',56,54]})
check.expect('t3',play_bingo(bgo_crd,[6]),'Winner: Row 3.')
check.expect('t3_mut',bgo_crd,{'O':[61,72,'XX',67,74],'I':[25,23,'XX',20,26],\
                                'N':[43,38,'XX',36,40],'B':['XX','XX','XX',\
                                                            'XX',10],\
                                'G':[56,53,'XX',47,52]})
check.expect('t4',play_bingo(my_card,[55,50,22]),no_win)
check.expect('t4_mut',my_card,{'O':[65,62,'XX',64,74],'I':['XX',25,'XX',20,26],\
                                'N':[41,45,'XX',33,43],'B':['XX','XX',14,\
                                                            'XX','XX'],\
                                'G':['XX',60,'XX',53,56]})
check.expect('t5',play_bingo(my_card,[14]),'Winner: Column B.')
check.expect('t5_mut',my_card,{'O':[65,62,'XX',64,74],'I':['XX',25,'XX',20,26],\
                                'N':[41,45,'XX',33,43],'B':['XX','XX','XX',\
                                                            'XX','XX'],\
                                'G':['XX',60,'XX',53,56]})
check.expect('t6',play_bingo(my_card_1,[14]),'Winner: Column B.')
check.expect('t6_mut',my_card_1,{'O':[65,62,'XX',64,74],'I':[22,25,'XX',20,26],\
                                'N':[41,45,'XX',33,43],'B':['XX','XX','XX',\
                                                            'XX','XX'],\
                                'G':[55,60,'XX',53,56]})

from random import randint

# make_bingo_card() returns a randomized Bingocard
# make_bingo_card: None -> Bingocard
def make_bingo_card():
    interval_width = 15
    card = {}
    for i in range(5):
        L = []
        while len(L) < 5:
            n = randint(interval_width*i+1,interval_width*(i+1))
            if not n in L:
                L.append(n)
                
        if i == 0:
            card['B'] = L
        elif i == 1:
            card['I'] = L
        elif i == 2:
            L[2] = 'XX'
            card['N'] = L
        elif i == 3:
            card['G'] = L
        else:
            card['O'] = L
    
    return card
