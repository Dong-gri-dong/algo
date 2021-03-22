import sys

sys.stdin = open("input_data/bj_2606_바이러스")

N = int(input())

E = int(input())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(E):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)


def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:

        v = Q.pop(0)

        for w in G[v]:

            if visited[w] != 0:
                continue

            Q.append(w)
            visited[w] =  1


bfs(1)
print(sum(visited)-1)