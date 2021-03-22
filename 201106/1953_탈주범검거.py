import sys
sys.stdin = open("input_data/1953_탈주범검거.txt")


T = int(input())
T = 1
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(N)]

    for i in arrs:
        print(*i)