import sys
sys.stdin = open("input_data/5249_최소신장트리.txt")

T = int(input())

for test_case in range(1, T+1):
    V , E = map(int, input().split())
    V += 1
    G = [[] for _ in range(V)]

    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))




    INF = 3123144
    def MST_PRIM(G, s): # G: 그래프, s: 시작 정점
        global key
        global pi
        global visited
        key = [INF] * V # 가중치를 무한대로 초기화
        pi = [[] for _ in range(V)] # 트리에서 연결된 부모 정점 초기화
        visited = [0]*V # 방문여부
        key[s] = 0 # 시작 정점의 가중치를 0으로 설정

        for _ in range(V): # 정점의 개수만큼 반복
            minindex = -1
            min = INF

            for i in range(V): # 방문 안한 정점중 최소 가중치 정점 찾기
                if not visited[i] and key[i] < min:
                    min = key[i]
                    minindex = i
            visited[minindex] = 1     # 최소 가중치 정점 방문처리

            for v, val in G[minindex]: # 선택 정점의 인접한 정점


                if not visited[v] and val < key[v]:
                    key[v] = val # 가중치 갱신
                    pi[v] = minindex # 트리에서 연결될 부모 정점



    MST_PRIM(G, 0)
    print('#{} {}'.format(test_case, sum(key)))




    def MST_PRIM(G, s): # G: 그래프, s: 시작 정점
        global key
        global pi
        global visited


        key = [INF] * V # 가중치를 무한대로 초기화
        pi = [[] for _ in range(V)] # 트리에서 연결된 부모 정점 초기화
        visited = [0]*V # 방문여부
        key[s] = 0 # 시작 정점의 가중치를 0으로 설정


        for _ in range(V): # 정점의 개수만큼 반복
            minindex = -1
            min = INF

            for i in range(V): # 방문 안한 정점중 최소 가중치 정점 찾기
                if not visited[i] and key[i] < min:
                    min = key[i]
                    minindex = i
            visited[minindex] = 1     # 최소 가중치 정점 방문처리

            for v, val in G[minindex]: # 선택 정점의 인접한 정점


                if not visited[v] and val < key[v]:
                    key[v] = val # 가중치 갱신
                    pi[v] = minindex # 트리에서 연결될 부모 정점