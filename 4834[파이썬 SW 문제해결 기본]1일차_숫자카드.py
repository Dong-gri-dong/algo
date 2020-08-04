import sys

sys.stdin = open('input_data/4834.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    counts = [0] * 10
    cards = input()

    for card in cards:
        counts[int(card)] += 1

    max_card_num = counts[0]
    for count in counts:
        if max_card_num < count:
            max_card_num = count

    for i in range(len(counts)-1,-1, -1):
        if counts[i] == max_card_num:
            max_card = i
            break


    print('#{} {} {}'.format(t, max_card, max_card_num))








    #print('#{} {}'.format(t, result_max-result_min))


