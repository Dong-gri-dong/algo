import sys
sys.stdin = open("input_data/5251_최소이동거리.txt")

T = int(input())
# for test_case in range(1, T+1):
#     N, E = map(int, input().split())
#     G = [[] for _ in range(N+1)]
#     for _ in range(E):
#         u, v, w =map(int, input().split())
#         G[u].append([v, w])
#         D = [0xffffff] * (N+1)
#         D[0] = 0
#         # if D[v] > D[u] + (u,v):
#         #     D[v] = D[u] + (u+v)
#         for u in range(N+1):
#             for v, w in G[u]:
#                 if D[v] > D[u] + w:
#                     D[v] = D[u] + w
#                     flag = False
#         if flag:
#             break
#     print(D[N])
# from collections import deque
# for test_case in range(1, T+1):
#     N, E = map(int, input().split())
#     G = [[] for _ in range(N+1)]
#     for _ in range(E):
#         u, v, w =map(int, input().split())
#         G[u].append([v, w])
#     D = [0xffffff] * (N+1)
#     D[0] = 0
#     Q = deque()
#     Q.append(0)
#     # if D[v] > D[u] + (u,v):
#     #     D[v] = D[u] + (u+v)
#     while Q:
#         u = Q.popleft()
#         for v, w in G[u]:
#             if D[v] > D[u] + w:
#                 D[v] = D[u] + w
#                 Q.append(v)
#
#     print(D[N])


from collections import deque
# for test_case in range(1, T+1):
#     N, E = map(int, input().split())
#     G = [[] for _ in range(N+1)]
#     for _ in range(E):
#         u, v, w =map(int, input().split())
#         G[u].append([v, w])
#     D = [0xffffff] * (N+1)
#     D[0] = 0
#     # Q = deque()
#     # Q.append(0)
#     # if D[v] > D[u] + (u,v):
#     #     D[v] = D[u] + (u+v)
#     def dfs(u):
#         for v, w in G[u]:
#             if D[v] > D[u] + w:
#                 D[v] = D[u] + w
#                 dfs(v)
#     dfs(0)
#
#     print(D[N])


for test_case in range(1, T+1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w =map(int, input().split())
        G[u].append([v, w])
    D = [0xffffff] * (N+1)
    D[0] = 0
    visit = [0] * (N + 1) #1: 선택된 정점(최단경로를 찾은 정점) 0: 선택안된 정점(최단경로 확정 x)
    cnt = 0
    while cnt <N + 1:
        u , Min = 0, 0xffffff
        for i in range(N+1):
            if visit[i] == 0 and Min > D[i]:
                u, Min = i, D[i]
        visit[u] = 1
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt += 1


    print(D[N])

