import sys

sys.stdin = open('input_data/1206.txt')

T = 10
for test_case in range(1, T + 1):
    result = 0
    total_num = int(input())
    N = list(map(int, input().split()))
    for i in range(2, total_num - 2):
        a = N[i - 2:i]
        a.extend(N[i+1:i+3])
        if N[i] > max(a):
            result += (N[i] - max(a))

    print('#{} {}'.format(test_case, result))
