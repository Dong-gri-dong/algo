import sys

sys.stdin = open("input_data/5102.txt")


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


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())

    G = [[] for _ in range(V+1)]
    visit = [0] * (V+1)


    for i in range(E):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)

    v, end = map(int, input().split())

    bfs(v)
    if visit[end] == 0:
        result = 0
    else:
        result = visit[end]-1
    print('#{} {}'.format(test_case, result))