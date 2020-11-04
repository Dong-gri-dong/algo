import sys
sys.stdin = open("input_data/가중치그래프")

V, E = map(int, input().split())

G = [[] for _ in range(V)]

for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
for i in G:
    print(*i)


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
        print(minindex)
        for v, val in G[minindex]: # 선택 정점의 인접한 정점


            if not visited[v] and val < key[v]:
                key[v] = val # 가중치 갱신
                pi[v] = minindex # 트리에서 연결될 부모 정점
        print(key)
        print()


MST_PRIM(G, 0)
print(pi)
print(key)
# print(visited)
# print(sum(key))