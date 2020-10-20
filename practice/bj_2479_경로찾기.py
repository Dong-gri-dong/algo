import sys

sys.stdin = open("input_data/bj_2479")

N, K = map(int,  input().split())


arrs = [ (map(int, input())) for _ in range(N)]


for i in arrs:
    print(*i)
