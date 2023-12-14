#https://adventofcode.com/2023/day/8
input_path = 'advent_2023_data/'


def extrapolate_vals(line, direction):
    if direction == 'forward':
        left_most_vals = [line[-1]]
    elif direction == 'backward':
        right_most_vals = [line[0]]
    while len([x for x in line if x != 0]) > 0:
        line = [line[i]-line[i-1] for i in range(1,len(line))]
        if direction == 'forward':
            left_most_vals.append(line[-1])
        elif direction == 'backward':
            right_most_vals.append(line[0])
    if direction == 'forward':
        return sum(left_most_vals)
    elif direction == 'backward':
        res = 0
        for val in right_most_vals[::-1]:
            res = val - res
        return res

def get_oasis_extrapolaion(file, pt):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()   
    lines = [line.strip().split(' ') for line in lines]
    lines = [[int(x) for x in line] for line in lines]
    res = 0
    for line in lines:
        if pt == 1:
            res += extrapolate_vals(line, 'forward')
        elif pt == 2:
            res += extrapolate_vals(line, 'backward')
    return res

def main():
    pt = 1
    print(get_oasis_extrapolaion(input_path + 'p9_data.txt', pt))

if __name__ == '__main__':
    main()
