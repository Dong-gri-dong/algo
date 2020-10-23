import sys

sys.stdin = open("input_data/bj_5427")


T = int(input())

dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]


def bfs(fire, people):
    global result
    Q = fire
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == w or ty < 0 or ty == h:
                continue
            if arrs[ty][tx] == '#' or visit[ty][tx] != 0:
                continue

            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1

    Q = people
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == w or ty < 0 or ty == h:
                continue
            if arrs[ty][tx] == '#':
                continue
            if visit[y][x] + 1 < visit[ty][tx]:
                result ='impossible'
                return
            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1



for test_case in range(1, T+1):
    result = 0
    w, h = map(int, input().split())
    arrs = [list(input()) for _ in range(h)]

    Q = []
    people = []
    fire = []
    goal = []
    for y in range(h):
        for x in range(w):
            if arrs[y][x] == '@':
                people.append([y ,x])
            elif arrs[y][x] == '*':
                fire.append([y,x])
            elif x == 0 or x == w - 1 or y == 0 or y == h - 1:
                goal.append([y][x])

    visit = [[0] * w for _ in range(h)]
    bfs(fire, people)

    # for y in range(h):
    #     for x in range(w):
    #         if x == 0 or x == w - 1 or y == 0 or y == h - 1:
    #             if visit[y][x]:
    #                 print(visit[y][x])
    print()
    for i in visit:
        print(*i)
    print(result)