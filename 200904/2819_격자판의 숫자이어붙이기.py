import sys

sys.stdin = open("input_data/2819.txt")

# T = int(input())
# N = 4
# #     상 하 좌 우
# dx = [ 0, 0, -1, 1]
# dy = [-1, 1,  0, 0]


# def seven(k, n, y, x):
#     global N
#
#     if k == n:
#         my_str = ''
#         for j in S:
#             my_str += str(j)
#         result.append(my_str)
#
#     else:
#         for i in range(4):
#             if x < 0 or x == N or y < 0 or y == N:
#                 return
#             S.append(G[y][x])
#             seven(k + 1, n, y + dy[i], x + dx[i])
#             S.pop()



def seven(k, n, y, x, numbers):
    global N
    if k == n:
        result.append(numbers)
        return
    else:
        for i in range(4):
            if x < 0 or x == N or y < 0 or y == N:
                return
            seven(k + 1, n, y + dy[i], x + dx[i], numbers + G[y][x] * 10**(n-k))


T = int(input())
N = 4
#     상 하 좌 우
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    G = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for y in range(N):
        for x in range(N):
            seven(0, 7, y, x, 0)
    print('#{} {}'.format(test_case, len(set(result))))







