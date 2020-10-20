import sys
sys.stdin = open("input_data/bj_2563")

N = int(input())

temp = [list(map(int, input().split())) for _ in range(N)]

arr = [[0]*100 for _ in range(100)]

size = 10
for i in range(len(temp)):
    for y in range(temp[i][0], temp[i][0]+size):
        for x in range(temp[i][1], temp[i][1] + size):
            arr[y][x] = 1

result = 0
for i in range(100):
    result += sum(arr[i])

print(result)