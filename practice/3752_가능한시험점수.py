
import sys

sys.stdin = open("input_data/3752.txt")




T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    total = 1 << N
    for i in range(total):
        sums = 0
        for j in range(N):
            if i & 1 << j:
                sums += arr[j]
        result.append(sums)
    print('#{} {}'.format(test_case, len(list(set(result)))))