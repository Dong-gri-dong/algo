import sys
sys.stdin = open("input_data/10726_이진수표현.txt")


T = int(input())

for test_case in range(1, T+1):
    result = 'ON'
    N, M = map(int, input().split())


    temp = bin(M)[2:]
    while len(temp) <= N:
        temp = '0'+temp



    for i in range(1, N+1):
        if temp[-i] == '0':
            result = 'OFF'

            break

    print('#{} {}'.format(test_case, result))



