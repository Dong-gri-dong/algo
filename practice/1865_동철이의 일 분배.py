import sys

sys.stdin = open("input_data/1865.txt")


def work(k, N, result):
    global percent
    if result <= percent:
        return

    if k == N:
        if percent <= result:
            percent = result
            return
    else:

        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                work(k + 1, N, result * arr[k][i] / 100)
                visit[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    visit = [0] * (N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    percent = 0
    work(0, N, 100)
    print('#{0} {1:0.6f}'.format(test_case, round(percent, 6)))

### 교수님 코드
def job(k,p): # k 함수 호출의 깊이, 직원의 번호
    global ans
    if k == N:
        ans = max(ans, p)
    else:
        for i in range(k, N): # k:기준위치, i: 순열로 선택할 위치
            if ans < p * G[k][order[i]]:
                order[k], order[i] = order[i], order[k]
                job(k+1, p * G[k][order[k]])
                order[k], order[i] = order[i], order[k]


ans = 100.0
col = [0] * N
for i in range(N):
    MAX, idx = 0, 0
    for j in range(N):
        if col[j] == 0 and MAX < G[i][k]:
            MAX, idx = G[i][j], j
    ans *= MAX
    col[idx] = 1

order = [x for x in range(N)] # 행 = 직원, 열 일
job(0, 100, 0)

