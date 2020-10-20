import sys

sys.stdin = open("input_data/7465.txt")

T = int(input())


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    visit = [0] * (N+1)


    for i in range(M):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)

    print(G)

    count = 0

    for v in range(1, N+1):
        if visit[v] == 1:
            continue
        count += 1
        S =[]
        S.append(v)
        visit[v] = 1
        while S:
            for w in G[v]:
                if visit[w] == 0:
                    visit[w] = 1
                    S.append(v)
                    v = w
                    break
            else:
                v = S.pop()

    print('#{} {}'.format(test_case, count))