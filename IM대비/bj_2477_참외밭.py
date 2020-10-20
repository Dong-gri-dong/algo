import sys
sys.stdin = open('input_data/bj_2477')


N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]
print(arr)


#1은 동쪽
#2은 서쪽
#3은 남쪽
#4은 북쪽


count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in range(len(arr)):
    if arr[i][0] == 1:
        count_1 += 1
    elif arr[i][0] == 2:
        count_2 += 1
    elif arr[i][0] == 3:
        count_3 += 1
    elif arr[i][0] == 4:
        count_4 += 1

print(count_1)
print(count_2)
print(count_3)
print(count_4)