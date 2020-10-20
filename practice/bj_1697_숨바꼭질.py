import sys
#from collections import deque



import sys
from collections import deque
#sys.stdin = open("input_data/bj_1697")
def bfs():
    Q = deque()
    Q.append(N)
    while Q:
        v1 = Q.popleft()
        if v1 == K:
            print(visit[v1])
            return
        for v2 in (v1-1, v1+1, 2*v1):
            if 0 <= v2 < maxs and not visit[v2]:
                visit[v2] = visit[v1] + 1
                Q.append(v2)


N, K = map(int, input().split())
maxs = 100001
visit = [0]*maxs
bfs()


#
#from collections import deque
def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)


MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()

