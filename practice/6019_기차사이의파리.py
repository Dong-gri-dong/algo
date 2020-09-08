import sys

sys.stdin = open("input_data/6019.txt")

T = int(input())

for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print('#{} {}'.format(test_case, F * D/(A+B)))