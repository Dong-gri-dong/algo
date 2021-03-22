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

    # D = [0xffffff] * (N+1)
    # D[0] = 0
    # visit = [0] * (N + 1) #1: 선택된 정점(최단경로를 찾은 정점) 0: 선택안된 정점(최단경로 확정 x)
    # cnt = 0
    # while cnt <N + 1:
    #     u , Min = 0, 0xffffff
    #     for i in range(N+1):
    #         if visit[i] == 0 and Min > D[i]:
    #             u, Min = i, D[i]
    #     visit[u] = 1
    #     for v, w in G[u]:
    #         if D[v] > D[u] + w:
    #             D[v] = D[u] + w
    #     cnt += 1
    #
    #
    # print(D[N])

    

    INF =312415141234
    # D: 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
    # P: 최단 경로 트리 저장
    def Dijkstra(G, r):
        global D
        D = [INF] * (N+1) # 처음에 무한대
        P = [[] for _ in range(N+1)]
        visited = [False] * (N+1) # 방문여부
        D[r] = 0  # 출발지의 가중치를 0으로

        for _ in range(N): # 최소 가중치 정점을 찾는 코드 이전에 프림과 동일
            minindex = -1
            min =INF
            for i in range(N):
                if not visited[i] and D[i] < min:
                    min = D[i]
                    minindex = i
            visited[minindex] = True
            for v, val in G[minindex]:
                if not visited[v] and D[minindex] + val < D[v]:
                    # 현재 정점에 인접한 정점에 대해 반복을 한다.
                    # 방문안한 정점중 선택한 정점의 가중치 값에 간선의 가중치를 더한값보다 v의 가중치더 크다면
                    # 이는 선택한 정점을 거쳐서 정접 v에 이르는 경로의 가중치합보다
                    # 지금까지 찾은 출발점에서 정점v까지 최단경로 가중치합이 더 큰지비교하는것
                    # 가중치가 작다면 더짧은 경로를 찾은것 그래서 값을 갱신해준다
                    D[v] = D[minindex] + val
                    P[v] = minindex

    Dijkstra(G, 0)
    print(D[N])


