import sys

sys.stdin = open("input_data/1861.txt")


T = int(input())
#     상  하  좌  우
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]


    max_count = 0
    max_value = 500000
    for y in range(N):
        for x in range(N):
            value = arr[y][x]
            count = 1
            while True:
                paths = 0
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]

                    if tx < 0 or tx == N or ty < 0 or ty == N:
                        continue
                    if arr[ty][tx] == arr[y][x] + 1:
                        x = tx
                        y = ty
                        count += 1
                        paths += 1
                        break

                else:
                    break

            if max_count < count:
                max_count = count
                max_value = value
            elif max_count == count:
                if max_value > value:
                    max_value = value



    print('#{} {} {}'.format(test_case, max_value ,max_count))
