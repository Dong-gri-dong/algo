import sys
sys.stdin = open("input_data/16926_배열돌리기1")

N, M, R = map(int, input().split())

arrs = [ list(map(int, input().split())) for _ in range(N) ]

for i in arrs:
    print(*i)

new_arr = []
for y in range(N):
    temp = []
    for x in range(M):
        temp.append(arrs[y][x])
    new_arr.append(temp)

j = 1
center = N//2
for y in range(N):
    for x in range(M):
        if y < center:

            if x < j:
                new_arr[y + 1][x] = arrs[y][x]
            elif j <= x <= M-j:
                new_arr[y][x-1] = arrs[y][x]
            else:
                new_arr[y-1][x] = arrs[y][x]

        elif y >= center:
            j -= 1
            if x < j:
                new_arr[y + 1][x] = arrs[y][x]
            elif j <= x <= M - j:
                new_arr[y][x+1] = arrs[y][x]
            else:
                new_arr[y - 1][x] = arrs[y][x]

        if y < center:
            j += 1



print()
for i in new_arr:
    print(*i)