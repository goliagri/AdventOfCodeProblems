#https://adventofcode.com/2023/day/14
input_path = 'advent_2023_data/'



def get_col_load(col):
    EMPTY_CHAR = '.'
    LOOSE_CHAR = 'O'
    FIXED_CHAR = '#'

    res = 0
    n = len(col)

    next_loc = 0
    for i, x in enumerate(col):
        if x == LOOSE_CHAR:
            res += n - i
    
    return res

def cycle(col):
    EMPTY_CHAR = '.'
    LOOSE_CHAR = 'O'
    FIXED_CHAR = '#'

    new_col = []
    next_loc = 0
    for i, x in enumerate(col):
        if x == EMPTY_CHAR:
            new_col.append(EMPTY_CHAR)
        elif x == LOOSE_CHAR:
            if next_loc < len(new_col):
                new_col[next_loc] = LOOSE_CHAR
                new_col.append(EMPTY_CHAR)
            else:
                new_col.append(LOOSE_CHAR)
            next_loc += 1
        elif x == FIXED_CHAR:
            new_col.append(FIXED_CHAR)
            next_loc = i + 1
    
    return new_col


def get_total_load(file, pt):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    
    cols = [[] for i in range(len(lines[0]))]
    for line in lines:
        for i in range(len(line)):
            cols[i].append(line[i])

    if pt == 2:
        history = []    
        num_cycles = 1000
        for i in range(num_cycles):
            next_cols = cols.copy()
            for k in range(4):
                for j, col in enumerate(next_cols):
                    next_cols[j] = cycle(col)
            #rotate next_cols matrix by 90 degrees 
                #print('-------------')
                #print_cols(next_cols)
                next_cols = list(zip(*next_cols))
                next_cols = next_cols[::-1]
                #print('!')
                #print_cols(next_cols)
            if next_cols in history:
                prev_idx = history.index(next_cols)
                loop_idx = (num_cycles - prev_idx) % (i - prev_idx)
                cols = history[prev_idx + loop_idx]
            history.append(next_cols)

    #translate cols back into rows and print
    print_cols(cols)
    res = 0
    for col in cols:
        if pt == 1:
            col = cycle(col)
        res += get_col_load(col)
    return res
            
def print_cols(cols):
    for i in range(len(cols[0])):
        for col in cols:
            print(col[i], end='')
        print('')


def main():
    pt = 2
    print(get_total_load(input_path + 'p14_example.txt', pt))

if __name__ == '__main__':
    main()