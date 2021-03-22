import sys
sys.stdin = open("input_data/bj_3190_뱀")

tx =[ 1, 0, -1, 0]
ty =[ 0, 1,  0, -1]

# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())
# 사과 위치
apple_arr = [list(map(int, input().split())) for _ in range(K)]
# 뱀의 방향 변환 횟수
L = int(input())
# x초가 끝난후에 방향회전
rotate_info = [list(input().split()) for _ in range(L)]
# 보드
arrs = [[0] * (N) for _ in range(N)]

for y, x in apple_arr:
    arrs[y-1][x-1] = 2





time = 1
rotate = 0
direction = 0

arrs[0][0] = 1
head = [0, 0]
tail = [0, 0]

while True:



    head[0] = head[0]+ty[direction]
    head[1] = head[1]+tx[direction]

    if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N or arrs[head[0]][head[1]] == 1:
        break




    if arrs[head[0]][head[1]] != 2:

        for i in range(4):
            if 0<= tail[0] + ty[i] <N and 0 <= tail[1] + tx[i] <N:
                if arrs[tail[0] + ty[i]][tail[1] + tx[i]] == 1:
                    arrs[tail[0]][tail[1]] = 0
                    tail[0] += ty[i]
                    tail[1] += tx[i]
                    break
    arrs[head[0]][head[1]] = 1


    if len(rotate_info) > rotate:
        if time == int(rotate_info[rotate][0]):
            if rotate_info[rotate][1] == 'D':
                direction = (direction + 1)%4
            else:
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            rotate += 1
    time += 1

print(time)






