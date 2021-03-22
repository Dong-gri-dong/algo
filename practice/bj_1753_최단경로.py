import sys
sys.stdin = open("input_data/bj_1753_최단경로")

N, E = map(int, input().split())
r = int(input())

G = [[] for _ in range(N+1)]

for i in range(E):
    s, e, v = map(int, input().split())
    G[s].append([e,v])


INF = 123123123
def Dijkstra(G, r):
    global D
    D = [INF] * (N + 1)
    P = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    D[r] = 0

    for _ in range(N):
        minindex = -1
        min = INF
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minindex = i
        visited[minindex] = True
        for v, val in G[minindex]:
            if not visited[v] and D[minindex] + val < D[v]:

                D[v] = D[minindex] + val
                P[v] = minindex

Dijkstra(G, r)

for i in D[1:]:
    if i == 123123123:
        print('INF')
    else:
        print(i)

