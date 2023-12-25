#https://adventofcode.com/2023/day/12
input_path = 'advent_2023_data/'

def num_possible_arrangements(layout, seq):
    OPPERATIONAL_CHAR = '.'
    DAMAGED_CHAR = '#'
    UNKNOWN_CHAR = '?'
    
    cache = {}
    def get_with_cache(layout_idx, seq, need_to_continue = False, need_to_not_continue = False):
        seq_tup = tuple(seq) #make hashable
        if (layout_idx, seq_tup, need_to_continue, need_to_not_continue) in cache:
            return cache[(layout_idx, seq_tup, need_to_continue, need_to_not_continue)]
        else:
            res = helper_num_arrangements(layout_idx, seq, need_to_continue, need_to_not_continue)
            cache[(layout_idx, seq_tup, need_to_continue, need_to_not_continue)] = res
            return res


    def helper_num_arrangements(layout_idx, seq, need_to_continue = False, need_to_not_continue = False):
        def try_repair_next(layout_idx, seq, need_to_continue, need_to_not_continue):
            if need_to_not_continue or not seq:
                return 0
            else:
                seq = seq.copy()
                seq[0] -= 1
                if seq[0] == 0:
                    seq.pop(0)
                    return get_with_cache(layout_idx+1, seq, need_to_not_continue=True)
                return get_with_cache(layout_idx+1, seq, need_to_continue=True)
            
        if layout_idx == len(layout):
            if seq == []:
                return 1
            else:
                return 0
        char = layout[layout_idx]
        if char == OPPERATIONAL_CHAR:
            if need_to_continue:
                return 0
            else:
                return get_with_cache(layout_idx+1, seq)
        elif char == DAMAGED_CHAR:
            return try_repair_next(layout_idx, seq, need_to_continue, need_to_not_continue)
        elif char == UNKNOWN_CHAR:
            if need_to_continue:
                return try_repair_next(layout_idx, seq, need_to_continue, need_to_not_continue)       
            elif need_to_not_continue or not seq:
                return get_with_cache(layout_idx+1, seq)
            else:
                res = try_repair_next(layout_idx, seq, need_to_continue, need_to_not_continue) + get_with_cache(layout_idx+1, seq)
                return res
    
    return helper_num_arrangements(0, seq)



def get_sum_possible_arrangements(file, pt):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]

    layouts = []
    seqs = []
    for line in lines:
        layouts.append(line.split(' ')[0])
        seqs.append([int(x) for x in line.split(' ')[1].split(',')])
    if pt == 2:
        layouts = ['?'.join([x]*5) for x in layouts]
        seqs = [seq*5 for seq in seqs]

    #print([num_possible_arrangements(layout, seq) for layout, seq in zip(layouts, seqs)])
    res = sum([num_possible_arrangements(layout, seq) for layout, seq in zip(layouts, seqs)])

    return res




def main():
    pt = 2
    print(get_sum_possible_arrangements(input_path + 'p12_data.txt', pt))


if __name__ == '__main__':
    main()