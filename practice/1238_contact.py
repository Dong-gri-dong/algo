import sys

sys.stdin = open("input_data/1238.txt")


T = 10
N = 100
for test_case in range(1,T+1):
    E, v = map(int, input().split())
    temp = list(map(int, input().split()))

    visited = [0] * (N+1)
    G = [[] for _ in range(N+1)]

    for i in range(int(E//2)):
        s, e = temp[2*i], temp[2*i+1]
        G[s].append(e)



    def BFS(v):
        Q = []

        Q.append(v)
        visited[v] = 1

        while Q:
            v = Q.pop(0)
            for w in G[v]:
                if visited[w] == 0:
                    Q.append(w)
                    visited[w] = visited[v] + 1

    BFS(v)

    max_idx = 0
    for i in range(1, N+1):
        if visited[max_idx] <= visited[i]:
            max_idx = i
    print('#{} {}'.format(test_case, max_idx))

