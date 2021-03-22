import sys

sys.stdin = open("input_data/1260_DFS와BFS")

N, M, v = map(int, input().split())


G = [ [] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)





def DFS(s):
    S = []
    S.append(s)
    visit[s] = 1
    print(s, end=' ')
    while S:

        for w in sorted(G[s]):

            if visit[w] != 1:
                visit[w] = 1
                S.append(s)
                print(w, end=' ')
                s = w
                break
        else:
            s = S.pop()



def BFS(s):
    Q = []
    Q.append(s)
    visit[s] = 1
    print(s, end=' ')
    while Q:

        s = Q.pop(0)
        for w in sorted(G[s]):
            if visit[w] == 0:
                print(w, end=' ')
                Q.append(w)
                visit[w] = visit[s] + 1



visit = [0] * (N + 1)
DFS(v)
print()
visit = [0] * (N + 1)
BFS(v)
