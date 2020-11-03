import sys
sys.stdin = open("input_data/6109_추억의 2048게임.txt")

T = int(input())

for test_case in range(1, T+1):
    N, action = input().split()
    N= int(N)
    arrs = [list(map(int, input().split())) for _ in range(N)]
    visit = [ [0]*N for _ in range(N) ]


    if action == 'up':
        for y in range(1, N):
            for x in range(0, N):
                if arrs[y-1][x]:
                    if arrs[y-1][x] == arrs[y][x]:
                        arrs[y-1][x] = 2*arrs[y-1][x]
                        visit[y-1][x] = 1
                        arrs[y][x] = 0
                else:
                    j = 0
                    while y-1-j >=0 and not arrs[y - 1 - j][x]:
                        arrs[y - 1 - j][x] = arrs[y - j][x]
                        arrs[y - j][x] = 0
                        j += 1

                    if  y-1-j >=0 and arrs[y - 1 - j][x] == arrs[y - j][x] and visit[y - 1 - j][x] == 0:
                        arrs[y - 1 - j][x] = 2 * arrs[y - 1- j][x]
                        visit[y - 1 - j][x] = 1
                        arrs[y-j][x] = 0

    elif action == 'down':
        for y in range(N-2, -1, -1):
            for x in range(N-1, -1, -1):

                if arrs[y + 1][x]:

                    if arrs[y + 1][x] == arrs[y][x]:
                        arrs[y + 1][x] = 2 * arrs[y + 1][x]
                        visit[y + 1][x] = 1
                        arrs[y][x] = 0
                else:
                    j = 0
                    while  + 1 + j < N and not arrs[y + 1 + j][x]:
                        arrs[y + 1 + j][x] = arrs[y + j][x]
                        arrs[y + j][x] = 0
                        j += 1

                    if y + 1 + j < N and arrs[y + 1 + j][x] == arrs[y + j][x]  and visit[y + 1 + j][x] == 0:
                        arrs[y + 1 + j][x] = 2 * arrs[y + 1 + j][x]
                        visit[y + 1 + j][x] = 1
                        arrs[y + j][x] = 0

    elif action == 'left':

        for x in range(1, N):
            for y in range(0, N):

                if arrs[y][x-1]:

                    if arrs[y][x - 1] == arrs[y][x]:
                        arrs[y][x - 1] = 2 * arrs[y][x - 1]

                        visit[y][x - 1] = 1

                        arrs[y][x] = 0

                else:

                    j = 0

                    while not arrs[y][x - 1 - j] and x - 1 - j >= 0:
                        arrs[y][x - 1 - j] = arrs[y][x - j]

                        arrs[y][x - j] = 0

                        j += 1

                    if arrs[y][x - 1 - j] == arrs[y][x - j] and x - 1 - j >= 0 and visit[y][x - 1 - j] == 0:
                        arrs[y][x - 1 - j] = 2 * arrs[y][x - 1 - j]

                        visit[y][x - 1 - j] = 1

                        arrs[y][x - j] = 0


    elif action == 'right':
        for x in range(N-2, -1, -1):
            for y in range(N-1, -1, -1):

                if arrs[y][x+1]:

                    if arrs[y][x + 1] == arrs[y][x]:
                        arrs[y][x + 1] = 2 * arrs[y][x + 1]

                        visit[y][x + 1] = 1

                        arrs[y][x] = 0

                else:

                    j = 0

                    while x + 1 + j < N and not arrs[y][x + 1 + j]:
                        arrs[y][x + 1 + j] = arrs[y][x + j]

                        arrs[y][x + j] = 0

                        j += 1

                    if  x + 1 + j < N and arrs[y][x + 1 + j] == arrs[y][x + j] and visit[y][x + 1 + j] == 0:
                        arrs[y][x + 1 + j] = 2 * arrs[y][x + 1 + j]
                        visit[y][x + 1 + j] = 1
                        arrs[y][x + j] = 0


    print('#{}'.format(test_case))
    for i in arrs:
        print(*i)
