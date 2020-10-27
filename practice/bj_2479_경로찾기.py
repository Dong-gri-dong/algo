import sys

sys.stdin = open("input_data/bj_2479")

N, K = map(int,  input().split())
arrs = [ list(map(int, input())) for _ in range(N)]
s, e = map(int, input().split())


G = [ [0]*(N+1) for _ in range(N+1)]


for i in range(len(arrs)):

    for j in range(1+i, len(arrs)):
        count = 0
        if arrs[i][0] != arrs[j][0]:
            count += 1
        if arrs[i][1] != arrs[j][1]:
            count += 1
        if arrs[i][2] != arrs[j][2]:
            count += 1
        G[i+1][j+1] =count
        G[j+1][i+1] =count



visit =[0]*(N+1)
temp = [ [] for _ in range(N+1) ]
temp[s].append(s)


def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)

        for w in range(0, (N+1)):
            if G[v][w] == 1 and visit[w] == 0:
                Q.append(w)

                visit[w] = visit[v] + 1
                for i in temp[v]:
                    temp[w].append(str(i) + str(w))
                if w == e:
                    return
bfs(s)

low_len = N
if temp[e]:
    for i in range(len(temp[e])):
        if low_len >= len(temp[e][i]):
            low_len = len(temp[e][i])
            result = temp[e][i]

    for k in result:
        print(k, end = ' ')
else:
    print(-1)



