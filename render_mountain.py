import check

# max_height(desc) returns the maximum height the mountain range correspond to
#   desc reached
# max_height: Str -> Nat
# requires: Str has only '+' and '-'
#           desc.count('+') =  desc.count('-')
#           s[0:n].count('+') >= s[0:n].count('-') for len(desc) >= n >= 0
# Examples:
# max_height('+++--+++---+-++---') => 4 
# max_height('+-') => 1 
# max_height('+++---') => 3 
# max_height('+-+-+-') => 1 
# max_height('') => 0

def max_height(desc):
    if desc == '': return 0
    m = 1
    for n in list(range(len(desc) + 1)):
        temp_height = desc[0:n].count('+') -  desc[0:n].count('-')
        if temp_height > m:
            m = temp_height
    return m

# Tests:
check.expect("test1_high",max_height('+++--+++---+-++---'),4)
check.expect("test2_high",max_height(''),0)
check.expect("test3_high",max_height('+-'),1)
check.expect("test4_high",max_height('+++---'),3)
check.expect("test5_high",max_height('+-+-+-'),1)
check.expect("test6_high",max_height('++--'),2)
check.expect("test7_high",max_height('+-++-+++-'),4)
check.expect("test8_high",max_height('++-+++----+-+++++-----'),5)
check.expect("test9_high",max_height('++-+--'),2)


# render_mountain(desc) returns a list of strings where the firsrt element is\
#   the top line of the mountain ranges' image, and the last element is the\
#   bottom line, all strings in the list have the same length, and are filled\
#   by spaces
# Effects: lst is mutated
# render_mountain: Str -> (listof Str)
# requires: Str has only '+' and '-'
#           desc.count('+') =  desc.count('-')
#           s[0:n].count('+') >= s[0:n].count('-') for len(desc) >= n >= 0
# Examples:
# render_mountain('++-++---') => ['    /\  ', ' /\/  \ ', '/      \\']
# render_mountain('+-') => ['/\\']
# render_mountain('') => []

def render_mountain(desc):
    if desc == '': return []
    high1 = max_height(desc)
    high2 = max_height(desc)
    down = '\\'
    lst = [['/']]
    while high1 != 1:
        lst.append([' '])
        high1 = high1 - 1
    index = 1
    while index != len(desc):
        row_num = desc[0:index].count('+') - desc[0:index].count('-')
        if desc[index] == '+':
            lst[row_num].append('/')
            for i in list(range(high2)):
                if i != row_num: lst[i].append(' ')
        else:
            lst[row_num - 1].append(down)
            for i in list(range(high2)):
                if i != row_num - 1: lst[i].append(' ')
        index = index + 1
    for i in list(range(len(lst))):
        lst[i] = ''.join(lst[i])
    lst.reverse()
    return lst
        
# Tests:
check.expect("test1_render",render_mountain('++-++---'),\
             ['    /\  ', ' /\/  \ ', '/      \\'])
check.expect("test2_render",render_mountain('+-'),\
             ['/\\'])
check.expect("test3_render",render_mountain(''),\
             [])
check.expect("test4_render",render_mountain('+-+-+-'),\
             ['/\/\/\\'])
check.expect("test5_render",render_mountain('++++----'),\
             ['   /\\   ', '  /  \\  ', ' /    \\ ', '/      \\'])
check.expect("test6_render",render_mountain('++-+--'),\
             [' /\\/\\ ', '/    \\'])
check.expect("test7_render",render_mountain('+-+-++-+-++---'),\
             ['          /\\  ', '     /\\/\\/  \\ ', '/\\/\\/        \\'])
check.expect("test8_render",render_mountain('++--'),\
             [' /\\ ', '/  \\'])
