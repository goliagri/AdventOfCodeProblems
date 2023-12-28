#https://adventofcode.com/2023/day/18
input_path = "advent_2023_data/"



def excavate(dig_orders):
    cur_pos = (0,0)
    excavated = set()
    for order in dig_orders:
        if order[0] == 'U':
            for i in range(order[1]):
                cur_pos = (cur_pos[0] - 1, cur_pos[1])
                excavated.add(cur_pos)
        elif order[0] == 'D':
            for i in range(order[1]):
                cur_pos = (cur_pos[0] + 1, cur_pos[1])
                excavated.add(cur_pos)
        elif order[0] == 'L':
            for i in range(order[1]):
                cur_pos = (cur_pos[0], cur_pos[1] - 1)
                excavated.add(cur_pos)
        elif order[0] == 'R':
            for i in range(order[1]):
                cur_pos = (cur_pos[0], cur_pos[1] + 1)
                excavated.add(cur_pos)
    return excavated

def dig_lagoon(file, pt):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines = [line.strip() for line in lines]
    dig_orders = [line.split(' ') for line in lines]
    dig_orders = [(x[0], int(x[1]), x[2][2:-1]) for x in dig_orders]
    excavated = excavate(dig_orders)    

    x_min = min([x[0] for x in excavated])
    x_max = max([x[0] for x in excavated])
    y_min = min([x[1] for x in excavated])
    y_max = max([x[1] for x in excavated])

    res = len(excavated)
    
    groups = []
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if not (i,j) in excavated:
                foundGroup = False
                neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
                to_remove = []
                for group in groups:
                    for neighbor in neighbors:
                        if neighbor in group:
                            if not foundGroup:
                                group.add((i,j))
                                cur_group = group
                                foundGroup = True
                                break
                            else:
                                cur_group |= group
                                to_remove.append(group)
                                break
                if not foundGroup:
                    groups.append(set([(i,j)]))
                else:
                    for rm in to_remove:
                        groups.remove(rm)
    
    #print(x_min, x_max, y_min, y_max)
    internal_group = []
    for group in groups:
        internal = True
        #print(group)
        for item in group:
            #print(group)
            if item[0] == x_min or item[0] == x_max or item[1] == y_min or item[1] == y_max:
                internal = False
                break
        if internal:
            internal_group.append(group)
    
    internal_group = set().union(*internal_group)
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if (i,j) in excavated:
                print('#', end='')
            elif (i,j) in internal_group:
                print('%', end='')
            else:
                print('.', end='')
        print()


    res += len(internal_group)

    return res
                            
    



def main():
    pt = 2
    print(dig_lagoon(input_path + "p18_data.txt", pt))

if __name__ == "__main__":
    main()