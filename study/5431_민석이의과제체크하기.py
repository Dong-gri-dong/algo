import sys
sys.stdin = open("input_data/5431_민석이의과제체크하기")
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    arrs = list(map(int, input().split()))

    check_list = list(range(1, N+1))

    for i in range(K):
        check_list.remove(arrs[i])

    print('#{} '.format(test_case), end='')
    for i in check_list:
        print(i, end=' ')
    print()

