import sys
sys.stdin = open("input_data/1974_스토쿠검증.txt")


T = int(input())


def check(arr):
    global result
    j = 1
    for i in sorted(arr):
        if i != j:
            result = 0
            return
        j += 1


for test_case in range(1, T + 1):
    result = 1
    arrs = [list(map(int, input().split())) for _ in range(9)]


    # 가로
    for y in range(9):
        check(arrs[y])



    # 세로
    v_arr = [[] for _ in range(9)]
    for y in range(9):
        for x in range(9):
            v_arr[x].append(arrs[y][x])
    for y in range(9):
        check(v_arr[y])



    # 3 x 3
    three_arr = []
    for y in range(0, 3):
        for x in range(0, 3):
            temp = []
            temp.extend(arrs[3*y][3*x:3*x + 3])
            temp.extend(arrs[3*y+1][3*x:3*x + 3])
            temp.extend(arrs[3*y+2][3*x:3*x + 3])
            three_arr.append(temp)

    for y in range(9):
       check(three_arr[y])

    print('#{} {}'.format(test_case, result))




