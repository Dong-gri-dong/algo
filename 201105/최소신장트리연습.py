import sys
sys.stdin = open("input_data/5249_최소신장트리.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    G = [[] for _ in range(V)]
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    for i in G:
        print(*i)
    INF = 1238379847
    def mst_prim(G, s):
        global key

        key = [INF] * V
        pi = [ [] for _ in range(V)]
        visit = [0] * V
        key[s] = 0

        for _ in range(V):
            minindex = -1
            min = INF

            for i in range(V):
                if not visit[i] and min > key[i]:

                    min = key[i]
                    minindex = i
            visit[minindex] =1

            for v, val in G[minindex]:
                if not visit[v] and  val < key[v]:
                    key[v] = val
                    pi[v] = minindex

    mst_prim(G, 0)
    print(sum(key))


    def mst_prim(G, s):
        key = [INF] * V
        pi = [ [] for _ in range(V)]
        visit = [0] * V
        pi[s] = 0

        for _ in range(V):
            min = INF
            minindex = -1
            for i in range(V):
                if visit[i] == 0 and min > key[i]:
                    min = key[i]
                    minindex = i
            visit[minindex] = 1
            for v, val in G[minindex]:
                if visit[v] == 0 and key[v] > val:
                    key[v] = val
                    pi[v] = minindex


    mst_prim(G, 0)
    print(sum(key))
