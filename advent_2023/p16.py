#https://adventofcode.com/2023/day/16
input_path = "advent_2023_data/"

def step_in_dir(i,j, dir):
    # 1 = up, 2 = right, 3 = down, 4 = left
    if dir == 1:
        return i-1, j, 1
    elif dir == 2:
        return i, j+1, 2
    elif dir == 3:
        return i+1, j, 3
    elif dir == 4:
        return i, j-1, 4 

def step(i,j, dir, char):
    if char == '.':
        return [step_in_dir(i,j,dir)]
    elif char == '|':
        if dir == 1 or dir == 3:
            return [step_in_dir(i,j,dir)]
        else:
            return [step_in_dir(i,j,1), step_in_dir(i,j,3)]
    elif char == '-':
        if dir == 2 or dir == 4:
            return [step_in_dir(i,j,dir)]
        else:
            return [step_in_dir(i,j,2), step_in_dir(i,j,4)]
    elif char == '/':
        if dir == 1:
            return [step_in_dir(i,j,2)]
        elif dir == 2:
            return [step_in_dir(i,j,1)]
        elif dir == 3:
            return [step_in_dir(i,j,4)]
        elif dir == 4:
            return [step_in_dir(i,j,3)]
    elif char == '\\':
        if dir == 1:
            return [step_in_dir(i,j,4)]
        elif dir == 2:
            return [step_in_dir(i,j,3)]
        elif dir == 3:
            return [step_in_dir(i,j,2)]
        elif dir == 4:
            return [step_in_dir(i,j,1)]
    else:
        raise ValueError("Invalid input char {}".format(char))
    


def energize_tiles(file, pt):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]

    if pt == 1: 
        return bfs(lines, (0,0,2))
    elif pt == 2:
        starts = []
        for i in range(len(lines)):
            starts.append((i,0,2))
            starts.append((i, len(lines[0])-1, 4))
        for j in range(len(lines[0])):
            starts.append((0,j,3))
            starts.append((len(lines)-1,j,1))
        return max([bfs(lines, start) for start in starts])

def bfs(lines, start):
    visited = set()
    frontier = [start]
    while frontier:
        row, col, dir = frontier.pop()
        if (row, col, dir) in visited or row < 0 or col < 0 or row >= len(lines) or col >= len(lines[0]):
            continue
        visited.add((row, col, dir))
        char = lines[row][col]
        frontier.extend(step(row, col, dir, char))
    
    visited_locs = set((x[0], x[1]) for x in visited)
    return len(visited_locs)


def main():
    pt = 2
    print(energize_tiles(input_path + "p16_data.txt", pt))


if __name__ == "__main__":
    main()