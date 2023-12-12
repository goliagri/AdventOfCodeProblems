#https://adventofcode.com/2023/day/8
input_path = 'advent_2023_data/'

'''
Note: part 2 of this problem is exceptionally poorly designed, I've implemented the intended solution which only works for an incredibly specific input that happens to be the case but isn't sepcified in the problem text.
A real solution to all valid inputs is much more complex.
'''
from functools import reduce
import math
def shortest_path_through_desert(file, pt):
    if pt == 1:
        start= 'AAA'
        target = 'ZZZ'
    elif pt == 2: #all nodes ending with given char are sarts/targets   
        start_char = 'A'
        target_char = 'Z'

    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    rl_instructs=  lines[0]
    nodes =  [line.split(' = ') for line in lines[2:]]
    network_dict = {node[0]: node[1].replace('(','').replace(')','').split(', ') for node in nodes}

    if pt == 1:
        cur_node = start
        rl_instruct_idx = 0
        count = 0
        while (pt == 1 and cur_node != target):
            if rl_instructs[rl_instruct_idx] == 'L':
                cur_node = network_dict[cur_node][0]
            elif rl_instructs[rl_instruct_idx] == 'R':
                cur_node = network_dict[cur_node][1]
            rl_instruct_idx = (rl_instruct_idx + 1) % len(rl_instructs)
            count += 1
    elif pt == 2:
        cur_nodes = [node for node in network_dict.keys() if node[-1] == start_char]
        print(cur_nodes)
        cycle_begin_idxs = []
        cycle_lens = []
        cycle_target_idxs = []
        for node in cur_nodes: #Note: we assume that all solutions lie in a cycle
            path = [(node,0)]
            rl_instruct_idx = 0
            while True:
                if rl_instructs[rl_instruct_idx] == 'L':
                    next = network_dict[path[-1][0]][0]
                elif rl_instructs[rl_instruct_idx] == 'R':
                    next = network_dict[path[-1][0]][1]
                if next[-1] == target_char:
                #if (next, rl_instruct_idx) in path: #cycle found
                    #cycle_begin_idxs.append(path.index((next, rl_instruct_idx)))
                    cycle_lens.append(len(path))
                    #cycle_target_idxs.append([i for i,x in enumerate(path[cycle_begin_idxs[-1]:]) if x[0][-1] == target_char])
                    break
                else:
                    path.append((next, rl_instruct_idx))
                    rl_instruct_idx = (rl_instruct_idx + 1) % len(rl_instructs)

        print(cycle_begin_idxs)
        print(cycle_lens)
        print(cycle_target_idxs)

        cycle_target_idxs = [target_idxs[0] for target_idxs in cycle_target_idxs] #We assume its always the first index for simplicity bc it does seem to be the case
        
        displacements = [cycle_begin_idx + cycle_target_idx for cycle_begin_idx, cycle_target_idx in zip(cycle_begin_idxs, cycle_target_idxs)]
        # we need to find smallest number n such that n % cycle_len_idxs[i] == displacements[i] for all i
    
        def solve_system_of_congruences(modulos, residues):
            #Returns smallest valuu n such that n === residues[i] (mod modulos[i]) for all i
            
            '''
            Steps: express as eqn -> substitute -> solve -> repeat
            in code: keep track of []
            '''
            n = len(modulos)

        def ExtendedEuclideanAlgorithm(a, b):
            """
                Calculates gcd(a,b) and a linear combination such that
                gcd(a,b) = a*x + b*y

                As a side effect:
                If gcd(a,b) = 1 = a*x + b*y
                Then x is multiplicative inverse of a modulo b.
            """
            aO, bO = a, b

            x = lasty = 0
            y = lastx = 1
            while b != 0:
                q = a / b
                a, b = b, a % b
                x, lastx = lastx - q * x, x
                y, lasty = lasty - q * y, y

            return {"x": lastx, "y": lasty, "gcd": aO * lastx + bO * lasty}


        def solveLinearCongruenceEquations(rests, modulos):
            """
            Solve a system of linear congruences.

            >>> solveLinearCongruenceEquations([4, 12, 14], [19, 37, 43])
            {'congruence class': 22804, 'modulo': 30229}
            """
            assert len(rests) == len(modulos)
            x = 0
            M = reduce(lambda x, y: x * y, modulos)

            for mi, resti in zip(modulos, rests):
                Mi = M / mi
                s = ExtendedEuclideanAlgorithm(Mi, mi)["x"]
                e = s * Mi
                x += resti * e
            return {"congruence class": ((x % M) + M) % M, "modulo": M}
        
        count = math.lcm(*cycle_lens)


    return  count

def main():
    pt = 2
    file = input_path + 'p8_data.txt'
    print(shortest_path_through_desert(file, pt))

if __name__ == '__main__':  
    main()