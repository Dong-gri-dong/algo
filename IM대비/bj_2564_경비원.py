import sys
sys.stdin = open("input_data/bj_2564")

# 가로 세로
X, Y = map(int, input().split())

N = int(input())

arr = [[0]*(X+1) for _ in range(Y+1)]


# 1 북족
# 2 남쪽
# 3 서쪽
# 4 동쪽
temp = [list(map(int, input().split())) for _ in range(N)]


y, w = map(int, input().split())
check = y
if y == 1:
    y = 0
    arr[y][w] = 1
    dong = [y,w]
elif y == 2:
    y = Y
    arr[y][w] = 1
    dong = [y, w]

elif y == 3:
    x = 0
    arr[w][x] = 1
    dong = [w, x]
else:
    x = X
    arr[w][x] = 1
    dong = [y, w-1]

print(dong)
result = 0
for i in range(N):
    y, w = temp[i]
    if y == 1:
        y = 0
        arr[y][w] = 1
        print(y, w)
        if check == 1:
            result += abs(w-dong[1])
        elif check == 2:
            result += Y
            if dong[0] > X//2:
                result += abs(X - dong[1])
                result += abs(X - w)

        elif check == 3:

        else:



    elif y == 2:
        y = Y
        arr[y][w] = 1
        print(y, w)
    elif y == 3:
        x = 0
        arr[w][x] = 1
        print(y, w)
    else:
        x = X
        arr[w][x] = 1
        print(y, w)


for i in arr:
    print(*i)