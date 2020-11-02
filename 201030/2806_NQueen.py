import sys
sys.stdin = open("input_data/2806_NQueen.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    visits = [[0] *N for _ in range(N)]

    def check(k, i):
        checks = []
        j = 0
        while k+j != N and i+j != N:
            if not visits[k+j][i+j]:
                visits[k+j][i+j] = 1
                checks.append([k+j, i+j])
            j += 1

        j = 0
        while k - j >= 0 and i - j >= 0:
            if not visits[k - j][i - j]:
                visits[k - j][i - j] = 1
                checks.append([k - j, i - j])
            j += 1
        j = 0
        while k - j >= 0 and i + j != N:
            if not visits[k - j][i + j]:
                visits[k - j][i + j] = 1
                checks.append([k - j, i + j])
            j += 1
        j = 0
        while k + j != N and i - j >= 0:
            if not visits[k + j][i - j]:
                visits[k + j][i - j] = 1
                checks.append([k + j, i - j])
            j += 1
        j = 0
        while k + j != N:
            if not visits[k + j][i]:
                visits[k + j][i] = 1
                checks.append([k + j, i])
            j += 1

        j = 0
        while i + j != N:
            if not visits[k][i + j]:
                visits[k][i + j] = 1
                checks.append([k, i + j])
            j += 1
        j = 0
        while i - j >= N:
            if not visits[k][i - j] :
                visits[k][i - j] = 1
                checks.append([k, i - j])
            j += 1


        return checks



    def keep(arrs):
        keep_arrs = []
        for y in range(N):
            temp = []
            for x in range(N):
                temp.append(arrs[y][x])
            keep_arrs.append(temp)
        return keep_arrs


    def queen(k):
        global count

        if k == N:
            count += 1
            return

        else:
            for i in range(N):
                if visits[k][i] == 0:
                    checks = check(k, i)
                    queen(k+1)
                    for y, x in checks:
                        visits[y][x] = 0


    count = 0
    queen(0)
    print('#{} {}'.format(test_case, count))
