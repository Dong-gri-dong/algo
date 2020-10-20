import sys
sys.stdin = open("input_data/bj_7569")

# M 가로
# N 세로
# H 높이
M, N, H = map(int,input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]

print(arr)


