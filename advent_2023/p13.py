#https://adventofcode.com/2023/day/13
input_path = 'advent_2023_data/'

def score_surface(surface, pt):
    HORIZONTAL_SCORE_MULTIPLIER = 1
    VERTICAL_SCORE_MULTIPLIER = 100
    #check for vertical symmetry
    for i in range(1,len(surface[0])-1):
        for j in range(len(surface)):
            is_symm = True
            for k in range(1, min(i+1, len(surface[0])-i)):
                if surface[j][i-k] != surface[j][i+k]:
                    is_symm = False
                    break
        if is_symm:
            print('!{}!'.format(i))
            return i * HORIZONTAL_SCORE_MULTIPLIER

    #check for horizontal symmetry
    for j in range(1,len(surface)-1):
        for i in range(len(surface[0])):
            is_symm = True
            for k in range(1, min(j+1, len(surface)-j)):
                if surface[j-k][i] != surface[j+k][i]:
                    is_symm = False
                    break
        if is_symm:
            print('!')
            return j * VERTICAL_SCORE_MULTIPLIER

def find_and_score_mirrors(file, pt):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    
    surfaces = [[]]
    for line in lines:
        if len(line) == 0:
            surfaces.append([])
        else:
            surfaces[-1].append(line)

    res = 0
    for surface in surfaces:
        res += score_surface(surface, pt)
    return res






def main():
    pt = 1
    print(find_and_score_mirrors(input_path + 'p13_example.txt', pt))



if __name__ == '__main__':
    main()