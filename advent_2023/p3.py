#https://adventofcode.com/2023/day/3
input_path = 'advent_2023_data/'

def sum_part_numbers(file):
    #reading from the file, we construct lists (number, set of adjacent coordinates), as well as a set of non-numerical non-period character coordinates. Then check or overlap
    f = open(file)
    lines = f.readlines()
    f.close()
    num_and_adjacency_list = []
    non_num_non_period_coords = set()
    cur_num_start = -1 #represents the col-index coordinate where the current number starts
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            if char.isdigit():
                if cur_num_start==-1:
                    cur_num_start = j
                if j==len(line)-1 or not line[j+1].isdigit():
                    above_set = set()
                    bellow_set = set()
                    if i>0:
                        above_set = set((i-1,x) for x in range(cur_num_start, j+1))
                        if j<len(line)-1:
                            above_set.add((i-1,j+1))
                        if cur_num_start>0:
                            above_set.add((i-1,cur_num_start-1))
                    if i<len(lines)-1:
                        bellow_set = set((i+1,x) for x in range(cur_num_start, j+1))
                        if j<len(line)-1:
                            bellow_set.add((i+1,j+1))
                        if cur_num_start>0:
                            bellow_set.add((i+1,cur_num_start-1))
                    equal_set = set()
                    if j<len(line)-1:
                        equal_set.add((i,j+1))
                    if cur_num_start>0:
                        equal_set.add((i,cur_num_start-1))
                    adj_set = above_set.union(bellow_set).union(equal_set)    
                    num_and_adjacency_list.append((int(line[cur_num_start:j+1]), adj_set))
                    cur_num_start = -1
            else:
                cur_num_start = -1
                if char!='.':
                    non_num_non_period_coords.add((i, j))
    res = 0
    for num, adj_set in num_and_adjacency_list:
        if not adj_set.isdisjoint(non_num_non_period_coords):
            res += num

def sum_gear_ratios(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    num_and_adjacency_list = []
    gear_coords = set()
    cur_num_start = -1 #represents the col-index coordinate where the current number starts
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            if char.isdigit():
                if cur_num_start==-1:
                    cur_num_start = j
                if j==len(line)-1 or not line[j+1].isdigit():
                    above_set = set()
                    bellow_set = set()
                    if i>0:
                        above_set = set((i-1,x) for x in range(cur_num_start, j+1))
                        if j<len(line)-1:
                            above_set.add((i-1,j+1))
                        if cur_num_start>0:
                            above_set.add((i-1,cur_num_start-1))
                    if i<len(lines)-1:
                        bellow_set = set((i+1,x) for x in range(cur_num_start, j+1))
                        if j<len(line)-1:
                            bellow_set.add((i+1,j+1))
                        if cur_num_start>0:
                            bellow_set.add((i+1,cur_num_start-1))
                    equal_set = set()
                    if j<len(line)-1:
                        equal_set.add((i,j+1))
                    if cur_num_start>0:
                        equal_set.add((i,cur_num_start-1))
                    adj_set = above_set.union(bellow_set).union(equal_set)    
                    num_and_adjacency_list.append((int(line[cur_num_start:j+1]), adj_set))
                    cur_num_start = -1
            else:
                cur_num_start = -1
                if char=='*':
                    gear_coords.add((i, j))
    res = 0
    gear_adj_lsts = [[] for _ in range(len(gear_coords))]
    for num, adj_set in num_and_adjacency_list:
        for i, coord in enumerate(gear_coords):
            if coord in adj_set:
                gear_adj_lsts[i].append(num)

    return sum([gear_adjs[0]*gear_adjs[1] for gear_adjs in gear_adj_lsts if len(gear_adjs)==2])

def main():
    pt=2
    if pt==1:
        print(sum_part_numbers(input_path + "p3_data.txt"))
    elif pt == 2:
        print(sum_gear_ratios(input_path + "p3_data.txt"))

if __name__ == "__main__":
    main()