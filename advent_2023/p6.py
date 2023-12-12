#https://adventofcode.com/2023/day/6
input_path = 'advent_2023_data/'
import math

def count_ways_to_beat_dist(t, d):
    # dist travelled = t-x * x, so (t-x) * x > d, x**2 - tx + d < 0, roots are t +/- sqrt(t**2 - 4*d) / 2
    if (t**2 - 4*d) <= 0: #imaginary roots, no way to beat dist
        return 0
    else: #real roots, return number of integers between them
        return max(0, math.floor((t + math.sqrt(t**2 - 4*d))/2) - math.ceil((t - math.sqrt(t**2 - 4*d))/2)) + 1

def count_races_solutions(file, pt):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line[line.index(':')+1:].strip() for line in lines]

    if pt == 1:
        Times = lines[0].split()
        Dists = lines[1].split()
        Times = [int(x) for x in Times if not x == '']
        Dists = [int(x) for x in Dists if not x == ''] 
    elif pt == 2:
        Time = int(lines[0].replace(" ", ""))
        Dist = int(lines[1].replace(" ", ""))

    if pt == 1:
        res = 1 
        for time, dist in zip(Times, Dists):
            res *= count_ways_to_beat_dist(time, dist)
        return res
    elif pt == 2:
        return count_ways_to_beat_dist(Time, Dist)



def main():
    pt = 2
    print(count_races_solutions(input_path + 'p6_data.txt', pt))


if __name__ == '__main__':
    main()  