#https://adventofcode.com/2023/day/4
input_path = 'advent_2023_data/'

def num_matches(scratch_str):
    scratch_str = scratch_str.strip()[scratch_str.index(':')+1:]
    winning_nums, chosen_nums = scratch_str.split(" | ")
    winning_nums = set(winning_nums.split(" "))
    chosen_nums = set(chosen_nums.split(" "))
    return len(winning_nums.intersection(chosen_nums) - set(['']))

def sum_scratchard_points(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    res = 0
    for line in lines:
        matches = num_matches(line)
        if matches:
            res += 2 ** (matches-1) 
    return res

def copy_scoring_scratchcards(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    copies = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        matches = num_matches(line)
        if matches: #currently does not handel case where we copy past end of file, we assume problem is constructed such that this wont happen
            copies[i+1:i+matches+1] = [x+copies[i] for x in copies[i+1:i+matches+1]]
    return sum(copies)



def main():
    pt = 2
    if pt == 1: 
        print(sum_scratchard_points(input_path + 'p4_data.txt')) 
    elif pt == 2:
        print(copy_scoring_scratchcards(input_path + 'p4_data.txt'))

if __name__ == '__main__':
    main()

