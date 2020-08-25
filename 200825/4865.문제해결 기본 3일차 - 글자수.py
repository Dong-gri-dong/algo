import sys
import pprint
sys.stdin = open('input_data/4865.txt')

T = int(input())


for t in range(1, 1+T):
    mains = list(input())
    targets = list(input())

    my_dict = dict()
    for i in mains:
        my_dict[i] = 0

    for i in targets:
        if i in mains:
            my_dict[i] += 1

    max_value = 0
    max_index = 0

    for idx, value  in my_dict.items():
        if max_value <= value:
            max_value = value
            max_index = idx

    print("#{} {}".format(t, max_value))
