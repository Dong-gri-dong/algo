import sys
sys.stdin = open("input_data/bj_2644")


N = int(input())

start, end = map(int, input().split())

E = int(input())

temp = [list(map(int, input().split())) for i in range(E)]

G = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for i in range(E):
    s, e = temp[i][0], temp[i][1]
    G[s].append(e)
    G[e].append(s)

def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if visit[w] == 0:
                Q.append(w)
                visit[w] = visit[v] + 1


bfs(start)

if visit[end]-1 == 0:
    print(-1)
else:
    print(visit[end]-1)