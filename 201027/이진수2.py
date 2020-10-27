import sys
sys.stdin = open("input_data/이진수2.txt")

T = int(input())

for test_case in range(1, T+1):
    flag = False
    N = float(input())
    sum = 0
    j = 1
    result = ''
    while N != 0:
        if N >= 1/2**j:
            N -= 1/2**j
            sum += 1 / 2 ** j
            result += '1'

        else:
            result += '0'
        j += 1
        if j >= 15:
            flag = True
            break
    if flag:
        print('#{} overflow'.format(test_case))
    else:
        print('#{} {}'.format(test_case, result))
