#https://adventofcode.com/2023/day/5
input_path = 'advent_2023_data/'

#map_type= 'scalars' OR 'ranges'
def get_locs(seeds, func_dict, map_type):
    cur_type = 'seed'
    cur_ids = seeds
    #print(seeds)
    while not cur_type == 'location':
        cur_type, cur_ids = run_almanac_func(func_dict[cur_type], cur_ids, map_type)
        #print(cur_type)
        #print(cur_ids)
    return cur_ids

#map_type= 'scalars' OR 'ranges'
def run_almanac_func(func_params, ids, map_type):
    output_type = func_params[0]
    output_ids = []
    for id in ids:
        if map_type == 'scalars':
            #id is a scalar
            found_mapping = False
            for dest_range_start, source_range_start, len in func_params[1]:
                if id >= source_range_start and id < source_range_start + len:
                    output_ids.append(dest_range_start + id - source_range_start)
                    found_mapping = True
                    break
            
            if not found_mapping:
                output_ids.append(id)
        elif map_type == 'ranges':
            #id is a tuple (range_start, length)
            mapped_ranges = [(float('-inf'), id[0])] #stores start and end of regions that have been mapped (NOT start,length)
            for dest_range_start, source_range_start, length in func_params[1]:
                id_start_greater_interv_start = id[0] >= source_range_start
                id_start_greater_interv_end = id[0] >= source_range_start + length
                id_end_greater_interv_end = id[0] + id[1] >= source_range_start + length
                id_end_less_interv_start = id[0] + id[1] <= source_range_start
                if id_start_greater_interv_end or id_end_less_interv_start:
                    continue
                elif id_start_greater_interv_start and id_end_greater_interv_end:
                    output_ids.append((dest_range_start- source_range_start + id[0] , source_range_start + length - id[0]))
                    mapped_ranges.append((id[0], source_range_start + length))
                elif id_start_greater_interv_start:
                    output_ids.append((dest_range_start - source_range_start + id[0] , id[1]))
                    mapped_ranges.append((id[0], id[0] + id[1]))
                elif id_end_greater_interv_end:
                    output_ids.append((dest_range_start, length))
                    mapped_ranges.append((source_range_start, source_range_start + length))
                else:
                    output_ids.append((dest_range_start, id[0] + id[1] - source_range_start))
                    mapped_ranges.append((source_range_start,id[0] + id[1]))
            mapped_ranges.append((id[0]+id[1],float('inf')))
            mapped_ranges.sort(key=lambda x: x[0])
            for i, rng in enumerate(mapped_ranges):
                if i == 0:
                    continue
                last_rng = mapped_ranges[i-1]
                if rng[0] != last_rng[1]:
                    output_ids.append((last_rng[1], rng[0] - last_rng[1]))
    return output_type, output_ids



def get_closest_seed_loc(file, pt):
    f = open(file)
    lines = f.readlines()
    f.close()
    #key is a string representing the input type
    #value is a tuple (string representing the output type, function parameters)
    specs = [[]]
    for line in lines:
        line = line.strip()
        if line == '':
            specs.append([])
        else:
            specs[-1].append(line)

    seed_spec = specs[0][0]
    func_specs = specs[1:]
    seeds = [int(x) for x in seed_spec[seed_spec.index(':')+1:].split(" ") if not x == '']
    if pt == 2:
        seeds = [(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds)//2)]

    func_dict = {}
    for func_spec in func_specs:
        func_name = func_spec[0]
        func_triples = func_spec[1:]
        src_name, _, dest_name = func_name[:-5].split('-')
        func_ranges = []
        for triple in func_triples:
            dest_range_start, src_range_start, length = triple.split(" ")
            src_range_start = int(src_range_start)
            dest_range_start = int(dest_range_start)
            length = int(length)
            func_ranges.append((dest_range_start, src_range_start, length))
        func_dict[src_name] = (dest_name, func_ranges)
    if pt==1:
        return min(get_locs(seeds, func_dict, map_type='scalars'))
    elif pt==2:
        return min([x[0] for x in get_locs(seeds, func_dict, map_type='ranges')])




def main():
    pt = 2
    print(get_closest_seed_loc(input_path + 'p5_data.txt', pt))

if __name__ == '__main__':
    main()