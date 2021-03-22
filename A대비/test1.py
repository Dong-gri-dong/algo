import sys
sys.stdin = open("input_data/test1")

# 가로 세로
N, M = map(int, input().split())

dx = [0, 1]
dy = [1, 0]
arrs = [list(map(int, input().split())) for _ in range(M)]


def cloth_count(y, x, count):
    global maxs

    if y == M - 1 and x == N - 1:
        if maxs <= count:
            maxs = count
        return
    else:
        for i in range(2):
            if 0 <= y + dy[i] < M and 0 < x + dx[i] < N:
                cloth_count(y + dy[i], x + dx[i], count + arrs[y + dy[i]][x + dx[i]])


maxs = 0
cloth_count(0, 0, arrs[0][0])
print(maxs)