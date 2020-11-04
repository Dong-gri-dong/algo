import sys
sys.stdin = open("input_data/가중치그래프")

V, E = map(int, input().split())

G = []

for i in range(E):
    u, v, w = map(int, input().split())
    G.append([u, v, w])




def make_set(vertice): # 부모정보 rank정보 배열만들기
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice): # 부모 노드를 찾는것
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2): # 집합 합치기
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

parent = [[] for _ in range(V)]
rank = [[] for _ in range(V)]

def MST_KRUSKAL(G):
    global mst

    mst = [] # 간선들의 집합 먼저 공집합을 생성
    for i in range(V): # 하나의 정점만 포함하는 상호배타집합을 정점의 수만큼 생성
        make_set(i)    # 부모정보와 rank정보를 담는 배열을 만들어줌

    G.sort(key = lambda x:x[2]) # 가중치를 기준으로 오름차순으로 정렬
    for i in G:
        print(*i)
    mst_cost = 0 # mst의 가중치를 누적할 변수
    while len(mst) < V-1: # 가중치가 낮은 간선을 선택하기 위한 부분 V-1개의 간선을 만듬
        u, v, val = G.pop(0)
        if find(u) != find(v): # 다른집합인지 검사하는 부분 같은 집합이면 사이클이 만들어지므로
            union(u, v)  # 다른 집합이면 정점끼리 집합을 이어줌 이때 rank를 기준으로
            mst.append((u, v)) # 트리에 (u,v)를 추가
            mst_cost += val

MST_KRUSKAL(G)
