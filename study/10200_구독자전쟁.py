import sys
sys.stdin = open("input_data/10200_구독자전쟁.txt")

T = int(input())

for test_case in range(1, T+1):
    N, A, B = map(int, input().split())
    maxs = min(A, B)
    mins = 0

    temp = max(A, B) - (N - maxs)
    if max(A, B) - (N - maxs) >0:
        mins = temp
    print('#{} {} {}'.format(test_case, maxs, mins))