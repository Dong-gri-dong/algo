import sys
sys.stdin = open("input_data/5567_결혼식")

N = int(input())
E = int(input())

G = [ [] for _ in range(N+1) ]
visit = [0] * (N+1)
for i in range(E):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)



def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if visit[w] != 0:
                continue
            Q.append(w)
            visit[w] = visit[v] + 1


bfs(1)

result = 0
for i in range(len(visit)):
    if visit[i] != 0 and visit[i] <= 3:
        result += 1
print(result-1)