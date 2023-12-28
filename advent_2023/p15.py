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
    if pt == 1:
        return sum([hash_func(step) for step in steps])
    elif pt == 2:
        boxes = [{} for i in range(256)]
        for i, step in enumerate(steps):
            if '=' in step:
                label, lense_val = step.split('=')
                hash_val = hash_func(label)
                if label in boxes[hash_val]:
                    boxes[hash_val][label] = (boxes[hash_val][label][0], lense_val)
                else:
                    boxes[hash_val][label] = (i, lense_val)
            elif '-' in step:
                label = step.split('-')[0]
                hash_val = hash_func(label)
                if label in boxes[hash_val]:
                    boxes[hash_val].pop(label)
            else:
                raise ValueError("No '=' or '-' found in step {}".format(step))
        boxes = [[y[1] for y in sorted(list(box_contents.values()), key=lambda x : x[0])] for box_contents in boxes]
        res = 0   
        for j, box in enumerate(boxes):
            for i in range(len(box)):
                res += int(box[i]) * (i+1) * (j + 1)
        return res


def main():
    pt = 2
    print(get_sum_of_hashes(input_path + "p15_data.txt", pt))

if __name__ == "__main__":
    main()
