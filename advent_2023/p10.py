#https://adventofcode.com/2023/day/8
input_path = 'advent_2023_data/'

def infer_next_from_start(grid, start):
    succs = []
    for i in range(1,5):
        if i == 1:
            next_coords = (start[0]+1, start[1], 1)
        elif i == 2:
            next_coords = (start[0], start[1]-1, 2)
        elif i == 3:
            next_coords = (start[0]-1, start[1], 3)
        elif i == 4:
            next_coords = (start[0], start[1]+1, 4)
        if not next_coords[:-1] in grid:
            continue
        if next(grid[next_coords[:-1]], next_coords) is not None:
            return next_coords
    raise Exception('No valid next pipe found')


def next(pipe_char, coords):
    #coords are (x, y, dir) where z is the direction (1-4) where the pipe came from
    #     1
    #   4 * 2
    #     3
    #returns None if the pipe does not accept the given input
    #pipes are given by characters that indicate direction, eg J connects direction 1 and 4
    row, col , dir = coords
    go_left = (row, col-1, 2)
    go_right = (row, col+1, 4)
    go_down = (row+1, col, 1)
    go_up = (row-1, col, 3)
    if pipe_char == '|':
        if dir == 1:
            return go_down
        elif dir == 3:
            return go_up
    elif pipe_char == '-':
        if dir == 2:
            return go_left
        elif dir == 4:
            return go_right
    elif pipe_char == 'L':
        if dir == 1:
            return go_right
        elif dir == 2:
            return go_up
    elif pipe_char == 'J':
        if dir == 1:
            return go_left
        elif dir == 4:
            return go_up
    elif pipe_char == '7':
        if dir == 3:
            return go_left
        elif dir == 4:
            return go_down
    elif pipe_char == 'F':
        if dir == 2:
            return go_down
        elif dir == 3:
            return go_right
    return None #if no matches to given pipe formats

def loop_len(file, pt):
    start_char = 'S'
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    grid = {}
    start = None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[(i,j)] = char
            if char == start_char:
                start = (i,j)
    if pt == 2:
        expanded_grid = {(i,j): '.' for i in range(len(lines)*2) for j in range(len(lines[0])*2)}
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                expanded_grid[(i*2,j*2)] = char
    if start is None:
        raise Exception('No starting character found found')
    

    cur_pos = infer_next_from_start(grid, start)
    cur_char = grid[cur_pos[:-1]]
    if pt == 2:
        adjusted_cur_pos = (cur_pos[0]*2, cur_pos[1]*2)
        in_loop = set()
        in_loop.add(cur_pos[:-1])
        in_loop.add((start[0]*2, start[1]*2))
        in_loop.add(adjusted_cur_pos[:-1])
        if cur_pos[2] == 1:
            in_loop.add((adjusted_cur_pos[0]-1, adjusted_cur_pos[1]))
        elif cur_pos[2] == 2:
            in_loop.add((adjusted_cur_pos[0], adjusted_cur_pos[1]+1))
        elif cur_pos[2] == 3:
            in_loop.add((adjusted_cur_pos[0]+1, adjusted_cur_pos[1]))
        elif cur_pos[2] == 4:
            in_loop.add((adjusted_cur_pos[0], adjusted_cur_pos[1]-1))
    elif pt == 1:
        loop_len = 1
    while cur_char != 'S':
        #print(cur_pos, cur_char)
        cur_pos = next(cur_char, cur_pos)
        #print(cur_pos)
        cur_char = grid[cur_pos[:-1]]
        if pt == 2:
            adjusted_cur_pos = (cur_pos[0]*2, cur_pos[1]*2)
            in_loop.add(adjusted_cur_pos[:-1])
            if cur_pos[2] == 1:
                in_loop.add((adjusted_cur_pos[0]-1, adjusted_cur_pos[1]))
            elif cur_pos[2] == 2:
                in_loop.add((adjusted_cur_pos[0], adjusted_cur_pos[1]+1))
            elif cur_pos[2] == 3:
                in_loop.add((adjusted_cur_pos[0]+1, adjusted_cur_pos[1]))
            elif cur_pos[2] == 4:
                in_loop.add((adjusted_cur_pos[0], adjusted_cur_pos[1]-1))
        elif pt == 1:
            loop_len += 1
    
    if pt == 2:
        #we transform by doubling grid dims to simulate connected components, use expanded grid for this
        

        coord_to_group_dict = {} #point -> all points connected to it excluding loop.
        for i in range(len(lines)*2):
            for j in range(len(lines[i])*2):
                if not (i,j) in in_loop:
                    adj_coords = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                    sets_to_union = []
                    for adj_coord in adj_coords:
                        if adj_coord in coord_to_group_dict:
                            sets_to_union.append(coord_to_group_dict[adj_coord])
                    if len(sets_to_union) > 0:
                        union = set()
                        for s in sets_to_union:
                            union.update(s)
                        union.add((i,j))
                        for key in coord_to_group_dict:
                            if coord_to_group_dict[key] in sets_to_union:
                                coord_to_group_dict[key] = union
                        coord_to_group_dict[(i,j)] = union

                    if not (i,j) in coord_to_group_dict:
                        coord_to_group_dict[(i,j)] = set()
                        coord_to_group_dict[(i,j)].add((i,j))
        
        enclosed_pts = set()
        for coord in coord_to_group_dict:
            #print(coord)
            #print(grid[coord])
            #print(coord_to_group_dict[coord])
            if set(x for x in coord_to_group_dict[coord] if x[0] == 0 or x[0] == len(lines)-1 or x[1] == 0 or x[1] == len(lines[x[0]])-1):
                coord_to_group_dict[coord].clear()
            if len(coord_to_group_dict[coord]) > 0:
                enclosed_pts.add(coord)
        
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if (i,j) in in_loop:
                    print('!', end='')
                elif (i,j) in enclosed_pts:
                    print('0', end='') 
                else:
                    print(' ', end='')
            print()
                 
        return len([pt for pt in enclosed_pts if pt[0] % 2 == 0 and pt[1] % 2 == 0]) #we select the real non-expanded points from the enclosed points
    elif pt == 1:
        return loop_len



def main():
    pt = 2
    if pt == 1:
        print((loop_len(input_path + 'p10_example_2.txt', pt)+1)//2)
    elif pt == 2:
        print(loop_len(input_path + 'p10_data.txt', pt))
    

if __name__ == '__main__':
    main()
