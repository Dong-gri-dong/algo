import sys
sys.stdin = open("input_data/가로세로합.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    arrs = [list(map(int, input().split())) for _ in range(N)]
    # print(arrs)

    print()
    for i in arrs:
        print(*i)
    print()

    def check(y,x):
        sums = 0
        for Y in range(N):
            for X in range(N):

                if X == x:
                    sums += arrs[Y][X]
                else:
                    if Y == y:
                        sums += arrs[Y][X]

        return sums


    result = 0
    max_x = 0
    max_y = 0

    for i in range(N):
        for j in range(N):

            temp = check(i, j)
            if result <= temp:
                result = temp
                max_x = j
                max_y = i

    # print('#{} {} {} {}'.format(test_case, max_y, max_x, result))
