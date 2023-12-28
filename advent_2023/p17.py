#https://adventofcode.com/2023/day/17
input_path = "advent_2023_data/"

import heapq


def get_succs(i,j, dir, num_consecutive):
    # up = 1, right = 2, down = 3, left = 4
    # can continue in the same direction or rotate 90 degrees. num_consecutive counts the number of steps we've taken in the current direction since the last rotation
    if dir == 1:
        return [(i-1, j, 1, num_consecutive + 1), (i, j+1, 2, 1), (i, j-1, 4, 1)]
    elif dir == 2:
        return [(i, j+1, 2, num_consecutive + 1), (i-1, j, 1, 1), (i+1, j, 3, 1)]
    elif dir == 3:
        return [(i+1, j, 3, num_consecutive + 1), (i, j+1, 2, 1), (i, j-1, 4, 1)]
    elif dir == 4:
        return [(i, j-1, 4, num_consecutive + 1), (i-1, j, 1, 1), (i+1, j, 3, 1)]
    else:
        raise ValueError("Invalid direction {}".format(dir))

def dykstras(lines, start, pt):
    # start is a tuple (i,j,dir, num_consecutive)
    visited = set(start)
    frontier = [(0,start)]
    while frontier: 
        curr = heapq.heappop(frontier)
        cost = curr[0]
        i,j,direction ,num_consecutive = curr[1]
        if i == len(lines) - 1 and j == len(lines[0]) - 1 and num_consecutive >= 4:
            return cost
        for succ in get_succs(i,j,direction,num_consecutive):
            if succ not in visited and ((pt==1 and succ[0] >= 0 and succ[0] < len(lines) and succ[1] >= 0 and succ[1] < len(lines[0]) and succ[3] <= 3) or
            (pt == 2 and succ[0] >= 0 and succ[0] < len(lines) and succ[1] >= 0 and succ[1] < len(lines[0]) and succ[3] <= 10 and (direction == succ[2] or num_consecutive >= 4))):
                heapq.heappush(frontier, (cost+int(lines[succ[0]][succ[1]]), succ))
                visited.add(succ)
    return None


def get_min_heat_loss_path(file, pt):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    return dykstras(lines, (0,0,2,0), pt)



def main():
    pt = 2
    print(get_min_heat_loss_path(input_path + "p17_data.txt", pt))

if __name__ == "__main__":
    main()