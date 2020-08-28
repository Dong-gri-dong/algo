import sys
#sys.stdin = open("input_data/bj_11724")

#
#
# N, E = map(int, input().split())
# temp = []
# for i in range(E):
#     temp.extend(list(map(int, input().split())))
#
# G = [[0] * (N+1) for _ in range((N+1))]
# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s][e] = G[e][s] = 1
#
#
#
# def dfs(v):
#
#     visited[v] = 1
#     cc.append(v)
#
#     for w in range(1, N+1):
#         if G[v][w] == 1 and visited[w] == 0:
#             dfs(w)
#
# result = []
# check = []
# count = 0
# for i in range(1, N+1):
#     if i not in check:
#         cc = []
#         visited = [0] * (N + 1)
#         dfs(i)
#         if cc not in result:
#             result.append(cc)
#             check.extend(cc)
#             count += 1
#
# print(count)





























import sys
N, E = map(int,sys.stdin.readline().split())
# s, e = map(int,sys.stdin.readline().split())

G = [[] for _ in range((N+1))]

for i in range(E):
    s, e = map(int,sys.stdin.readline().split())
    G[s].append(e)
    G[e].append(s)






visited = [0] * (N + 1)

count = 0
for v in range(1, N+1):
    if visited[v] == 1:
        continue

    S = [v]
    visited[v] = 1


    while S:

        for w in G[v]:
            if visited[w] == 0:
                visited[w] = 1
                S.append(v)
                v = w
                break
        else:
             v = S.pop()

    count += 1


print(count)