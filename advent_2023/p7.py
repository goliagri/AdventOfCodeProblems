#https://adventofcode.com/2023/day/7
input_path = 'advent_2023_data/'

import heapq

def get_hand_rank_val(hand, jokers=False):
    #assigns an integer value to the hand representing its 'strenght' in ranking. A lower value denotes a higher rank
    if not jokers:
        strengths = {'A':1, 'K':2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13}
    else:
        strengths = {'A':1, 'K':2, 'Q':3, 'J':14, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13} #j's are now lowest ranked

    count = {}
    for card in hand:
        count[card] = count.get(card, 0) + 1
    
    if jokers:
        j_count = count.get('J', 0)
        if j_count != 0:
            count.pop('J')
    
    count = sorted(count.values(), reverse=True)
    if jokers and j_count:
        if count:
            count[0] += j_count #imporant note: the optimal joker strategy is always to add to the dominant card type in hand.
        else: #if every card is a joker, make a 5 of a kind
            count.append(j_count)

    if count[0] == 5: #5 of a kind
        res = 0
    elif count[0] == 4: #4 of a kind
        res = 1
    elif count[0] == 3 and count[1] == 2: #full house
        res = 2
    elif count[0] == 3: #3 of a kind
        res = 3
    elif count[0] == 2 and count[1] == 2: #2 pairs
        res = 4
    elif count[0] == 2: #1 pair
        res = 5
    else: #high card
        res = 6
    res *= 1e10 #card type strength is the leading digit of integer value, meaning it will be the first in the comparison.

    for i, card in enumerate(hand[::-1]): #construct integer such that card strengths will be compared left to right after the leading digit.
        res += strengths[card] * 10**(i*2) 
    return res

def get_set_winnings(file, pt):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    lines = [line.strip().split(" ") for line in lines]
    # each line = [hand, bet], both strs

    rank_list = []
    for hand, bet in lines:
        if pt == 1:
            heapq.heappush(rank_list, (get_hand_rank_val(hand, jokers=False), int(bet)))
        if pt == 2:
            heapq.heappush(rank_list, (get_hand_rank_val(hand, jokers=True), int(bet)))
    
    res = 0
    i = len(rank_list)
    while rank_list:
        res += i * heapq.heappop(rank_list)[1]
        i -= 1
    return res

def main():
    pt = 1
    print(get_set_winnings(input_path + 'p7_data.txt', pt))


if __name__ == '__main__':
    main()