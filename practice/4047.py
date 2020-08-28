import sys
import pprint
sys.stdin = open('input_data/4047.txt')

T = int(input())


for test_case in range(1, T+1):
    result = 1

    my_dict = {
        'S': 13, 'D': 13,
        'H': 13, 'C': 13
    }

    N = input()
    new_N = []
    for i in range(int(len(N)//3)):
        new_N.append(N[(3*i): (3*i)+3])


    if len(list(new_N)) != len(set(new_N)):
        result = "ERROR"


    for i in new_N:
        my_dict[i[0]] -= 1

    print('#{}'.format(test_case), end=' ')

    if result == 1:
        for i in my_dict.values():
            print(i, end=' ')
        print()
    else:
        print(result)





