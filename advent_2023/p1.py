#https://adventofcode.com/2023/day/1
input_path = "advent_data/"
def get_calibration_value_pt1(text):
    text = list(filter(lambda x: x.isdigit(), text))
    if not text:
        raise ValueError("No digits found in text {}".format(text))
    return int(text[0] + text[-1])

def get_calibration_value_pt2(text):
    dig_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first_dig = None
    #find first digit
    for i in range(len(text)):
        if text[i].isdigit():
            first_dig = text[i]
            break
        for dig_str in dig_strs:
            if i < len(text)-(len(dig_str)-1) and text[i:i+len(dig_str)] == dig_str:
                first_dig = str(dig_strs.index(dig_str) + 1)
                break
        if first_dig:
            break

    last_dig = None
    #find first digit
    for i in range(len(text)-1, -1, -1):
        if text[i].isdigit():
            last_dig = text[i]
            break
        for dig_str in dig_strs:
            if i >= len(dig_str) and text[i-len(dig_str)+1:i+1] == dig_str:
                last_dig = str(dig_strs.index(dig_str) + 1)
                break
        if last_dig:
            break
        
    if first_dig is None or last_dig is None:
        raise ValueError("No digits or digit words found in text {}".format(text))
    
    print(int(first_dig + last_dig))
    return int(first_dig + last_dig)

def calibrate_file_and_sum(file, pt = 2):
    f = open(file)
    lines = f.readlines()
    f.close()
    if pt == 1:
        res = sum([get_calibration_value_pt1(line) for line in lines])
    elif pt == 2:
        res = sum([get_calibration_value_pt2(line) for line in lines])
    return res



def main():
    print(calibrate_file_and_sum(input_path + "p1_data.txt"))

if __name__ == "__main__":
    main()
