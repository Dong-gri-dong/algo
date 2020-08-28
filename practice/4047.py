import sys
import pprint
sys.stdin = open('input_data/4047.txt')

T = int(input())


my_dict ={
    'S' : 0, 'D' : 1,
    'H' : 2, 'C' : 3
}
for test_case in range(1, T+1):
    my_arr = [[0] * 13 for _ in range(4)]
    result = 1


    N = input()

    for i in range(4):



        if my_arr[ my_dict[str(N[3*i])] ][ int(N[(3*i)+1:(3*i)+3])] == 0:
            my_arr[my_dict[str(N[3 * i])]][int(N[(3 * i) + 1:(3 * i) + 3])] = 1
        else:
            result = 0
            break

    print('#{}'.format(test_case), end=" ")
    if not result:
        print('ERROR', end="")
    else:
        for i in range(4):
            print(13 - sum(my_arr[i]), end =" ")
    print()

