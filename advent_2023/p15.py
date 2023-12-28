#https://adventofcode.com/2023/day/15
input_path = "advent_2023_data/"

def hash_func(x):
    res = 0
    for c in x:
        res  += ord(c)
        res *= 17
        res %= 256
    return res

def get_sum_of_hashes(file, pt):
    f = open(file)
    text = f.read()
    f.close()
    text = text.strip()
    steps = text.split(',')
    return sum([hash_func(step) for step in steps])


def main():
    pt = 1
    print(get_sum_of_hashes(input_path + "p15_data.txt", pt))

if __name__ == "__main__":
    main()
