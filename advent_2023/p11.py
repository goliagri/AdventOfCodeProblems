#https://adventofcode.com/2023/day/11
input_path = 'advent_2023_data/'






def sum_shortest_galactic_paths(file, pt):

    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]

    cols_with_galaxy = set()
    rows_with_galaxy = set()

    if pt == 2:
        added_cols = set()
        added_rows = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                cols_with_galaxy.add(j)
                rows_with_galaxy.add(i) 
    print(cols_with_galaxy, rows_with_galaxy)

    for line in lines:
        print(line)
    offset = 0
    for i in range(len(lines[0])):
        if i not in cols_with_galaxy:
            lines = [line[:i+offset] + '.' + line[i+offset:] for line in lines]
            if pt == 2:
                added_cols.add(i+offset)
            offset += 1
    print('-----------------------------------------------')
    offset = 0
    for i in range(len(lines)):
        if i not in rows_with_galaxy:
            lines.insert(i+offset, '.'*len(lines[0]))
            if pt == 2:
                added_rows.add(i+offset)
            offset += 1

    for line in lines:
        print(line)
    
    galaxy_coords = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                galaxy_coords.add((i,j))

    galaxy_coords = list(galaxy_coords)

    res = 0
    for i, galaxy_1 in enumerate(galaxy_coords):
        for galaxy_2 in galaxy_coords[i+1:]:
            res += abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])
            if pt == 2:
                ADDED_SPACE_COST = 100 - 1
                lower_x = min(galaxy_1[0], galaxy_2[0])
                upper_x = max(galaxy_1[0], galaxy_2[0])
                for x in range(lower_x+1, upper_x):
                    if x in added_cols:
                        res += ADDED_SPACE_COST - 1
                lower_y = min(galaxy_1[1], galaxy_2[1])
                upper_y = max(galaxy_1[1], galaxy_2[1])
                for y in range(lower_y+1, upper_y):
                    if y in added_rows:
                        res += ADDED_SPACE_COST - 1
    
    return res
    



def main():
    pt = 2
    print(sum_shortest_galactic_paths(input_path + 'p11_example.txt', pt))


if __name__ == '__main__':
    main()