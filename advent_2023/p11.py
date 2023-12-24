#https://adventofcode.com/2023/day/11
input_path = 'advent_2023_data/'

class SegmentTreeNode:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.lazy = 0

        if start != end:
            mid = (start + end) // 2
            self.left = SegmentTreeNode(start, mid)
            self.right = SegmentTreeNode(mid+1, end)
    
    def update(self, start, end, val):
        if start > self.end or end < self.start:
            return
        elif start <= self.start and end >= self.end:
            self.val += val * (self.end - self.start + 1)
            self.lazy += val
            return
        else:
            self.left.update(start, end, val)
            self.right.update(start, end, val)
            self.val = self.left.val + self.right.val + self.lazy * (self.end - self.start + 1)

    def query(self, start, end):
        if start > self.end or end < self.start:
            return 0
        if start <= self.start and end >= self.end:
            return self.val
        
        if self.lazy != 0:
            self.left.update(self.lazy)
            self.right.update(self.lazy)
            self.lazy = 0

        return self.left.query(start, end) + self.right.query(start, end)



def sum_shortest_galactic_paths(file, pt):

    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]

    cols_with_galaxy = set()
    rows_with_galaxy = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                cols_with_galaxy.add(j)
                rows_with_galaxy.add(i) 


    col_expansions = SegmentTreeNode(0, len(lines[0]))
    for i in range(len(lines[0])):
        if not i in cols_with_galaxy:
            col_expansions.update(i, i, 1)

    row_expansions = SegmentTreeNode(0, len(lines))
    for i in range(len(lines)):
        if not i in rows_with_galaxy:
            row_expansions.update(i, i, 1)

    if pt == 1:
        expansion_factor = 2
    elif pt == 2:
        expansion_factor = 1000000

    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies.append((i,j))
    
    res = 0
    for i, galaxy_1 in enumerate(galaxies):
        for j, galaxy_2 in enumerate(galaxies[i+1:]):
            lower_x = min(galaxy_1[0], galaxy_2[0])
            upper_x = max(galaxy_1[0], galaxy_2[0])
            lower_y = min(galaxy_1[1], galaxy_2[1])
            upper_y = max(galaxy_1[1], galaxy_2[1])
            res += upper_x - lower_x + upper_y - lower_y #manhattan distance
            res += col_expansions.query(lower_y, upper_y) * (expansion_factor - 1)
            res += row_expansions.query(lower_x, upper_x) * (expansion_factor - 1)

    return res


def main():
    pt = 2
    print(sum_shortest_galactic_paths(input_path + 'p11_data.txt', pt))


if __name__ == '__main__':
    main()