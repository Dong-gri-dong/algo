import sys

sys.stdin = open("input_data/1267_1.txt")


def bfs(v):
    # print(v)
    if visit[v] == 0:
        pass
    elif visit[v] == check_list[v]:
        return
    Q = []
    Q.append(v)
    visit[v] += 1
    while Q:

        v = Q.pop(0)
        result.append(v)
        for w in range(1, N + 1):
            if G[v][w] == 1:
                if visit[w] == check_list[w] - 1:
                    Q.append(w)
                    visit[w] += 1

                elif visit[w] != check_list[w] - 1:
                    visit[w] += 1


def check(N):
    a = [0] * (N + 1)
    for i in range(1, N+1):
        for k in range(1, N + 1):
            a[k] += G[i][k]
    return a

for test_case in range(1, 11):
    N, E = map(int, input().split())

    temp = list(map(int, input().split()))

    G = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        G[s][e] = 1


    start_point = []
    check_list = check(N)

    for j in range(max(check_list)+1):
        for i in range(1, N+1):
            if check_list[i] == j:
                start_point.append(i)

    visit = [0] * (N + 1)
    result = []

    for v in start_point:
        bfs(v)

    print('#{}'.format(test_case), end = ' ')
    for i in result:
        print(i, end = ' ')
    print()
