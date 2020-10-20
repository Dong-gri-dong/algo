import sys
sys.stdin = open("input_data/bj_2578")

arr = [list(map(int, input().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))


def check(number):
    global result
    for y in range(5):
        count_x = 0
        count_y = 0
        for x in range(5):
            if arr[y][x] == 0:
                count_y += 1
            if count_y == 5:
                result += 1
            if arr[x][y] == 0:
                count_x += 1
            if count_x == 5:
                result += 1
    count_1 = 0
    count_2 = 0
    for i in range(5):
        if arr[i][i] ==0:
            count_1 += 1
        if count_1 == 5:
            result += 1
        if arr[i][5-i-1] == 0:
            count_2 += 1
        if count_2 == 5:
            result += 1

flag = False
counts = 0
for i in numbers:
    if flag:
        break
    for y in range(5):
        if flag:
            break
        for x in range(5):
            if flag:
                break
            result = 0
            if arr[y][x] == i:

                arr[y][x] = 0
                counts += 1
                check(i)

            if result >= 3:
                flag = True
                print(counts)
                break