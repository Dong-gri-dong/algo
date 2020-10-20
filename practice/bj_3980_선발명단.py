import sys
sys.stdin = open("input_data/bj_3980")

T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(11)]

    # for i in arr:
    #     print(*i)

    def position(k, N, score):
        global best
        if k == N:
            if best < score:
                best = score
            return
        else:
            for i in range(N):
                if arr[i][k] != 0 and visit[i] == 0:
                    visit[i] = 1
                    position(k+1, N, score+arr[i][k])
                    visit[i] = 0

    best = 0
    visit = [0] * 11
    position(0, 11, 0)
    print(best)