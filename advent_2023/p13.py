#https://adventofcode.com/2023/day/13
input_path = 'advent_2023_data/'

def score_surface(surface, pt):
    HORIZONTAL_SCORE_MULTIPLIER = 1
    VERTICAL_SCORE_MULTIPLIER = 100
    NUM_SMUDGES = 1
    #check for vertical symmetry
    for i in range(1,len(surface[0])):
        if pt == 1:
            is_symm = True
        elif pt == 2:
            symm_breakers = 0
        for j in range(len(surface)):
            for k in range(0, min(i, len(surface[0])-i)):
                if surface[j][i-1-k] != surface[j][i+k]:
                    if pt == 1:
                        is_symm = False
                        break
                    elif pt == 2:
                        symm_breakers += 1
                        if symm_breakers > NUM_SMUDGES:
                            break
        if (pt == 1 and is_symm) or (pt == 2 and symm_breakers == NUM_SMUDGES):
            return i * HORIZONTAL_SCORE_MULTIPLIER

    #check for horizontal symmetry
    for j in range(1,len(surface)):
        if pt == 1:
            is_symm = True
        elif pt == 2:
            symm_breakers = 0
        for i in range(len(surface[0])):
            for k in range(0, min(j, len(surface)-j)):
                if surface[j-1-k][i] != surface[j+k][i]:
                    if pt == 1:
                        is_symm = False
                        break
                    elif pt == 2:
                        symm_breakers += 1
                        if symm_breakers > NUM_SMUDGES:
                            break
        if (pt == 1 and is_symm) or (pt == 2 and symm_breakers == NUM_SMUDGES):
            return j * VERTICAL_SCORE_MULTIPLIER
    for line in surface:
        print(line)
    raise Exception('No symmetry found')

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
    pt = 2
    print(find_and_score_mirrors(input_path + 'p13_data.txt', pt))



if __name__ == '__main__':
    main()