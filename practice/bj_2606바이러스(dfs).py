import sys
sys.stdin = open("input_data/bj_2606")

N = int(input())
E = int(input())
temp = []
for _ in range(E):
    temp.extend(list(map(int, input().split())))




visited = [0] * (N+1)
G = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = G[e][s] = 1


def dfs(v):
    visited[v] = 1

    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

    return visited



count = -1
for i in dfs(1):
    if i == 1:
        count += 1

print(count)
