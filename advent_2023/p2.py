#https://adventofcode.com/2023/day/2
import math 

input_path = 'advent_2023_data/'

def is_possible_game(game, contents):
    for key in game:
        if game[key] > contents[key]:
            return False
    return True

def get_power(min_game_cubes):
    return math.prod(min_game_cubes.values())

def sum_possible_game_ids(file, contents={'red':12, 'green':13, 'blue':14}, pt=2):
    f = open(file)
    lines = f.readlines()
    f.close()
    res = 0
    for i, line in enumerate(lines):
        line_after_id = line[line.index(':')+1:]
        game_dict = {}
        for game_el in line_after_id.split(';'):
            for num_color_pair in game_el.split(','):
                num, color = num_color_pair.strip().split(' ')
                num = int(num)
                game_dict[color] = max(game_dict.get(color, 0), num)
        if pt==1 and is_possible_game(game_dict, contents):
            res += i+1
        elif pt==2:
            res += get_power(game_dict)

    return res
            
            
    
def main():
    print(sum_possible_game_ids(input_path + "p2_data.txt"))

if __name__ == "__main__":
    main()